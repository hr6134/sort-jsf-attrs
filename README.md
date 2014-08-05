Help in sorting tag's attributes in jsf files.
Order of attributes set in attr_order variable.
Useful as hook for git, mercurial or other VCS. It's help to keep all attributes in same order, so xhtmls will be ease to read.
As example, next tag:
'''xhtml
<a4j:commandButton value="#{commonBundle.update}"
                   styleClass="linkIcon"
                   render="panel"
                   id="someId"
                   limitRender="true"
                   action="#{bean.update}"
                   execute="@form"
                   image="/images/search_icon_32.png"/>
'''
will transform to this
'''xhtml
<a4j:commandButton id="someId"
                   value="#{commonBundle.update}"
                   action="#{bean.update}"
                   execute="@form"
                   styleClass="linkIcon"
                   render="panel"
                   limitRender="true"
                   image="/images/search_icon_32.png"/>
'''
