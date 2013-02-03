from Acquisition import aq_inner

from plone.app.portlets.interfaces import IPortletPermissionChecker
from plone.app.portlets.browser import editmanager as base


class ManagePortletAssignments(base.ManagePortletAssignments):
    """This view allows to delete even broken portlet assignment"""

    # view @@delete-portlet
    def delete_portlet(self, name):
        assignments = aq_inner(self.context)
        IPortletPermissionChecker(assignments)()

        # set fixing_up to True to let zope.container.contained
        # know that our object doesn't have __name__ and __parent__
        from zope.container  import contained
        fixing_up = contained.fixing_up
        contained.fixing_up = True

        del assignments[name]

        # revert our fixing_up customization
        contained.fixing_up = fixing_up

        self.request.response.redirect(self._nextUrl())
        return ''
