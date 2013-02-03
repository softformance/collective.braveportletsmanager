from Acquisition import aq_inner

from plone.portlets.utils import unhashPortletInfo
from plone.app.portlets.utils import assignment_mapping_from_key

from plone.app.portlets.interfaces import IPortletPermissionChecker

from plone.app.portlets.browser import kss as base


class PortletManagerKSS(base.PortletManagerKSS):
    """Customized version that allows removal of broken portlet assignments"""

    def delete_portlet(self, portlethash, viewname):
        info = unhashPortletInfo(portlethash)
        assignments = assignment_mapping_from_key(self.context,
                        info['manager'], info['category'], info['key'])

        IPortletPermissionChecker(assignments.__of__(aq_inner(self.context)))()


        # set fixing_up to True to let zope.container.contained
        # know that our object doesn't have __name__ and __parent__
        from zope.container  import contained
        fixing_up = contained.fixing_up
        contained.fixing_up = True

        del assignments[info['name']]

        # revert our fixing_up customization
        contained.fixing_up = fixing_up

        return self._render_column(info, viewname)
