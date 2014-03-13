#@+leo-ver=5-thin
#@+node:cmsxh.20131226100304.3661: * @file application
#
# -*- coding: utf-8 -*-
'''
Copyright © 2014 Chiaming Yen

CMSimply is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CMSimply is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CMSimpiy. If not, see <http://www.gnu.org/licenses/>.

***********************************************************************
'''

#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:cmsxh.20131226100304.3662: ** <<declarations>> (application)
import cherrypy
import re
import os
import math
import hashlib
from cherrypy.lib.static import serve_file
# use quote_plus() to generate URL
import urllib.parse
# use cgi.escape() to resemble php htmlspecialchars()
# use cgi.escape() or html.escape to generate data for textarea tag, otherwise Editor can not deal with some Javascript code.
import cgi

# get the current directory of the file
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
import sys
sys.path.append(_curdir)

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    inOpenshift = True
else:
    inOpenshift = False

if inOpenshift:
    # while program is executed in OpenShift
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # while program is executed in localhost
    download_root_dir = _curdir
    data_dir = _curdir

#@-<<declarations>>
#@+others
#@+node:cmsxh.20131226100304.3663: ** downloadlist_access_list
def downloadlist_access_list(files, starti, endi):
    # different extension files, associated links were provided
    # popup window to view images, video or STL files, other files can be downloaded directly
    # files are all the data to list, from starti to endi
    # add file size
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(download_root_dir+"downloads/"+files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # stl files
        elif fileExtension == ".stl":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/static/viewstl.html?src=/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # flv files
        elif fileExtension == ".flv":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/flvplayer?filepath=/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # direct download files
        else:
            outstring += "<input type='checkbox' name='filename' value='"+files[index]+"'><a href='/download/?filepath="+download_root_dir.replace('\\', '/')+ \
            "downloads/"+files[index]+"'>"+files[index]+"</a> ("+str(fileSize)+")<br />"
    return outstring
#@+node:cmsxh.20140108172857.1763: ** sizeof_fmt
def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
#@+node:cmsxh.20131226100304.3664: ** set_admin_css
# set_admin_css for administrator
def set_admin_css():
    outstring = '''<!doctype html><html><head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>CMSimply - Simple Cloud CMS in Python 3</title> \
<link rel="stylesheet" type="text/css" href="/static/cmsimply.css">
'''+syntaxhighlight()

    outstring += '''
<script src="/static/jquery.js"></script>
<script type="text/javascript">
$(function(){
    $("ul.topmenu> li:has(ul) > a").append('<div class="arrow-right"></div>');
    $("ul.topmenu > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
});
</script>
'''
    # SSL for OpenShift operation
    if inOpenshift:
        outstring += '''
<script type="text/javascript">
if ((location.href.search(/http:/) != -1) && (location.href.search(/login/) != -1)) \
window.location= 'https://' + location.host + location.pathname + location.search;
</script>
'''
    site_title, password = parse_config()
    outstring += '''
</head><header><h1>'''+site_title+'''</h1> \
<confmenu>
<ul>
<li><a href="/">Home</a></li>
<li><a href="/sitemap">SiteMap</a></li>
<li><a href="/edit_page">Edit All</a></li>
<li><a href="'''+cherrypy.url(qs=cherrypy.request.query_string)+'''&edit=1">Edit</a></li>
<li><a href="/edit_config">Config</a></li>
<li><a href="/search_form">Search</a></li>
<li><a href="/imageuploadform">Image Upload</a></li>
<li><a href="/fileuploadform">File Upload</a></li>
<li><a href="/download_list">File List</a></li>
<li><a href="/logout">Logoout</a></li>
'''
    outstring += '''
</ul>
</confmenu></header>
'''
    return outstring
#@+node:cmsxh.20131226100304.3665: ** set_footer
def set_footer():
    # Extra consideration for cherrypy.url(qs=cherrypy.request.query_string) return no data
    return "<footer> \
        <a href='/edit_page'>Edit All</a>| \
        <a href='"+cherrypy.url(qs=cherrypy.request.query_string)+"&edit=1'>Edit</a>| \
        <a href='/edit_config'>Config</a> \
        <a href='/login'>login</a>| \
        <a href='/logout'>logout</a> \
        <br />Powered by <a href='http://cmsimple.cycu.org'>CMSimply</a> \
        </footer> \
        </body></html>"
#@+node:cmsxh.20131226100304.3666: ** file_get_contents
def file_get_contents(filename):
    # open file in utf-8 and return file content
    with open(filename, encoding="utf-8") as file:
        return file.read()
#@+node:cmsxh.20131226100304.3667: ** search_content
# use head title to search page content
def search_content(head, page, search):
    return page[head.index(search)]
#@+node:cmsxh.20131226100304.3668: ** parse_content
def parse_content():
    if not os.path.isfile(data_dir+"content.htm"):
        # create content.htm if there is no content.htm
        File = open(data_dir+"content.htm", "w", encoding="utf-8")
        File.write("<h1>head 1</h1>content 1")
        File.close()
    subject = file_get_contents(data_dir+"content.htm")
    # deal with content without heading
    # replace subject content with special seperate string to avoid error 
    subject = re.sub('#@CMSIMPLY_SPLIT@#', '井@CMSIMPLY_SPLIT@井', subject)
    content_sep = '#@CMSIMPLY_SPLIT@#'
    head_level = 3
    content = re.split('</body>', subject)
    result = re.sub('<h[1-'+str(head_level)+']>', content_sep, content[0])
    # remove the first element contains html and body tags
    data = result.split(content_sep)[1:]
    head_list = []
    level_list = []
    page_list = []
    order = 1
    for index in range(len(data)):
        #page_data = re.sub('</h[1-'+str(head_level)+']>', content_sep, data[index])
        page_data = re.sub('</h', content_sep, data[index])
        head = page_data.split(content_sep)[0]
        order += 1
        head_list.append(head)
        # put level data into level variable
        level = page_data.split(content_sep)[1][0]
        level_list.append(level)
        # remove  1>,  2> or 3>
        page = page_data.split(content_sep)[1][2:]
        page_list.append(page)
    return head_list, level_list, page_list
#@+node:cmsxh.20131226100304.3669: ** render_menu
def render_menu(head, level, page, sitemap=0):
    directory = ""
    current_level = level[0]
    if sitemap:
        directory += "<ul>"
    else:
        directory += "<ul id='css3menu1' class='topmenu'>"
    for index in range(len(head)):
        if level[index] > current_level:
            directory += "<ul>"
            directory += "<li><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
        elif level[index] == current_level:
            if level[index] == 1:
                if sitemap:
                    directory += "<li><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
                else:
                    directory += "<li class='topmenu'><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
            else:
                directory += "<li><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
        else:
            directory += "</li>"*(int(current_level) - int(level[index]))
            directory += "</ul>"*(int(current_level) - int(level[index]))
            if level[index] == 1:
                if sitemap:
                    directory += "<li><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
                else:
                    directory += "<li class='topmenu'><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
            else:
                directory += "<li><a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a>"
        current_level = level[index]
    directory += "</li></ul>"
    return directory
#@+node:cmsxh.20131226100304.3670: ** filebrowser
def filebrowser():
    return '''
<script type="text/javascript">
function wrFilebrowser (field_name, url, type, win) {
poppedUpWin = win;
inputField = field_name;
if (type == "file") {type = "downloads"};
var cmsURL = "/file_selector";    

if (cmsURL.indexOf("?") < 0) {
    cmsURL = cmsURL + "?type="+ type ;
}
else {
    cmsURL = cmsURL + "&type="+type ;
}

tinyMCE.activeEditor.windowManager.open(
    {
        file  : cmsURL,
        width : 800,
        height : 600,
        resizable : "yes",
        inline : "yes",
        close_previous : "no",
        popup_css : false,
        scrollbars : "yes"
      },
      {
        window : win,
        input : field_name
      }
);
return false;
}
'''
#@+node:cmsxh.20131226100304.3671: ** syntaxhighlight
def syntaxhighlight():
    return '''
<script type="text/javascript" src="/static/syntaxhighlighter/shCore.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushJScript.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushJava.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushPython.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushSql.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushXml.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushPhp.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCpp.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCss.js"></script>
<script type="text/javascript" src="/static/syntaxhighlighter/shBrushCSharp.js"></script>
<link type="text/css" rel="stylesheet" href="/static/syntaxhighlighter/css/shCoreDefault.css"/>
<script type="text/javascript">SyntaxHighlighter.all();</script>
'''
#@+node:cmsxh.20131226100304.3672: ** editorhead
def editorhead():
    return '''
<script language="javascript" type="text/javascript" src="/static/tinymce3/tiny_mce/tiny_mce.js"></script>
<script type="text/javascript" src="/static/tinymce3/init.js"></script>
'''
#@+node:cmsxh.20131226100304.3673: ** tinymceinit
def tinymceinit():
    return '''
<script language="javascript" type="text/javascript">
function tinyMCE_initialize0() {
    tinyMCE_instantiateByClasses('simply-editor', {
// General options

theme : "advanced",
width : "800",
height : "600",
element_format : "html",
language : "en",
plugins : "autosave,pagebreak,style,layer,table,save,advimage,advlink,advhr,emotions,iespell,"
        + "insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,"
        + "noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,media,lists,syntaxhl",

// Theme options
theme_advanced_buttons1 : "save,|,fullscreen,code,formatselect,fontselect,fontsizeselect,styleselect,syntaxhl",
theme_advanced_buttons2 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,cut,copy,paste,pastetext,pasteword,|,bullist,numlist,outdent,indent,blockquote",
theme_advanced_buttons3 : "undo,redo,|,link,unlink,anchor,image,media,cleanup,|,hr,removeformat,visualaid,|,forecolor,backcolor,|,search,replace,|,charmap",
theme_advanced_buttons4 : "emotions,sub,sup,|,tablecontrols,insertdate,inserttime,help",
theme_advanced_toolbar_location : "top",
theme_advanced_toolbar_align : "left",
theme_advanced_statusbar_location : "bottom",
theme_advanced_resizing : true,
theme_advanced_blockformats : "h1,h2,h3,p,div,h4,h5,h6,blockquote,dt,dd,code",
theme_advanced_font_sizes : "8px=8px, 10px=10px,12px=12px, 14px=14px, 16px=16px, 18px=18px,20px=20px,24px=24px,36px=36px",

content_css : "/static/cmsimply.css",
//link and image list
external_image_list_url: "/static/tinymce3/cms_image_list.js",
external_link_list_url: "/static/tinymce3/cms_link_list.js",

// Extra
plugin_insertdate_dateFormat: "%d-%m-%Y",
plugin_insertdate_timeFormat: "%H:%M:%S",
inline_styles : true,
apply_source_formatting : true,
relative_urls : true,
convert_urls: false,
entity_encoding : "raw",

file_browser_callback: "wrFilebrowser" ,
fullscreen_new_window : false ,
fullscreen_settings : {
theme_advanced_buttons1: "save,|,fullscreen,code,|,formatselect,fontselect,fontsizeselect,styleselect,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,cut,copy,paste,pastetext,pasteword,|,bullist,numlist,outdent,indent,blockquote,|,undo,redo",
theme_advanced_buttons2 : "link,unlink,anchor,image,media,cleanup,|,hr,removeformat,visualaid,|,forecolor,backcolor,|,search,replace,|,charmap,emotions,|,sub,sup,tablecontrols,insertdate,inserttime,|,help",
theme_advanced_buttons3 : "",
theme_advanced_buttons4 : ""
}
});
}
</script>
'''
#@+node:cmsxh.20131226100304.3674: ** editorfoot
def editorfoot():
    return '''<body id="body"  onload="tinyMCE_initialize0();">'''
#@+node:cmsxh.20131226100304.3675: ** tinymce_editor
def tinymce_editor(menu_input=None, editor_content=None, page_order=None):
    files = os.listdir(download_root_dir+"downloads/")
    link_list = ""
    image_list = ""
    for index in range(len(files)):
        file_url = "/download/?filepath="+download_root_dir.replace('\\', '/')+"downloads/"+files[index]
        link_list += "['"+files[index]+"', '"+file_url+"']"
        if index != len(files)-1:
            link_list += ","
    # deal with image link
    images = os.listdir(download_root_dir+"images/")
    for index in range(len(images)):
        image_url = "/images/"+images[index]
        image_list += "['"+images[index]+"', '"+image_url+"']"
        if index != len(images)-1:
            image_list += ","
    sitecontent =file_get_contents(data_dir+"content.htm")
    editor = set_admin_css()+editorhead()+filebrowser()+'''
var myImageList = new Array('''+image_list+''');
var myLinkList = new Array('''+link_list+''');
</script>'''+tinymceinit()+'''</head>'''+editorfoot()
    # edit all pages
    if page_order == None:
        outstring = editor + "<div class='container'><nav>"+ \
            menu_input+"</nav><section><form method='post' action='savePage'> \
     <textarea class='simply-editor' name='page_content' cols='50' rows='15'>"+editor_content+"</textarea> \
     <input type='submit' value='save'></form></section></body></html>"
    else:
        # add viewpage button wilie single page editing
        head, level, page = parse_content()
        outstring = editor + "<div class='container'><nav>"+ \
            menu_input+"</nav><section><form method='post' action='ssavePage'> \
     <textarea class='simply-editor' name='page_content' cols='50' rows='15'>"+editor_content+"</textarea> \
<input type='hidden' name='page_order' value='"+str(page_order)+"'> \
     <input type='submit' value='save'>"
        outstring += '''<input type=button onClick="location.href='get_page?heading='''+head[page_order]+ \
            ''''" value='viewpage'></form></section></body></html>'''
    return outstring
#@+node:cmsxh.20131226100304.3676: ** parse_config
def parse_config():
    if not os.path.isfile(data_dir+"config"):
        # create config file if there is no config file
        file = open(data_dir+"config", "w", encoding="utf-8")
        # default password is admin
        password="admin"
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        file.write("siteTitle:CMSimply - Simple Cloud CMS in Python 3\npassword:"+hashed_password)
        file.close()
    config = file_get_contents(data_dir+"config")
    config_data = config.split("\n")
    site_title = config_data[0].split(":")[1]
    password = config_data[1].split(":")[1]
    return site_title, password
#@+node:cmsxh.20131226100304.3677: ** file_selector_script
def file_selector_script():
    return '''
<script type="text/javascript" src="/static/tinymce3/tiny_mce/tiny_mce_popup.js"></script>
<script language="javascript" type="text/javascript">

var FileBrowserDialogue = {
    
    init : function () {
        // Nothing to do
    },

   
    submit : function (url) {
        var URL = url;
        var win = tinyMCEPopup.getWindowArg("window");
        var input = win.document.getElementById(tinyMCEPopup.getWindowArg("input"));
        win.document.getElementById(tinyMCEPopup.getWindowArg("input")).value = URL;

        input.value = URL;
        if (input.onchange) input.onchange();

        tinyMCEPopup.close();
    }
}

tinyMCEPopup.onInit.add(FileBrowserDialogue.init, FileBrowserDialogue);

function setLink(link){

    FileBrowserDialogue.submit(link);
    return true;
}
</script>
'''
#@+node:cmsxh.20131226100304.3678: ** file_lister
def file_lister(directory, type=None, page=1, item_per_page=10):
    files = os.listdir(download_root_dir+directory)
    total_rows = len(files)
    totalpage = math.ceil(total_rows/int(item_per_page))
    starti = int(item_per_page) * (int(page) - 1) + 1
    endi = starti + int(item_per_page) - 1
    outstring = file_selector_script()
    notlast = False
    if total_rows > 0:
        outstring += "<br />"
        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
        if int(page) > 1:
            outstring += "<a href='"
            outstring += "/file_selector?type="+type+"&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>Previous</a> "
        span = 10
        for index in range(int(page)-span, int(page)+span):
        #for ($j=$page-$range;$j<$page+$range;$j++)
            if index>= 0 and index< totalpage:
                page_now = index + 1 
                if page_now == int(page):
                    outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                else:
                    outstring += "<a href='"
                    outstring += "/file_selector?type="+type+"&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                    outstring += "'>"+str(page_now)+"</a> "

        if notlast == True:
            nextpage = int(page) + 1
            outstring += " <a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>>></a><br /><br />"
        if (int(page) * int(item_per_page)) < total_rows:
            notlast = True
            if type == "downloads":
                outstring += downloadselect_access_list(files, starti, endi)+"<br />"
            else:
                outstring += imageselect_access_list(files, starti, endi)+"<br />"
        else:
            outstring += "<br /><br />"
            if type == "downloads":
                outstring += downloadselect_access_list(files, starti, total_rows)+"<br />"
            else:
                outstring += imageselect_access_list(files, starti, total_rows)+"<br />"
        if int(page) > 1:
            outstring += "<a href='"
            outstring += "/file_selector?type="+type+"&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'><<</a> "
            page_num = int(page) - 1
            outstring += "<a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>Previous</a> "
        span = 10
        for index in range(int(page)-span, int(page)+span):
        #for ($j=$page-$range;$j<$page+$range;$j++)
            if index >=0 and index < totalpage:
                page_now = index + 1
                if page_now == int(page):
                    outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                else:
                    outstring += "<a href='"
                    outstring += "/file_selector?type="+type+"&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                    outstring += "'>"+str(page_now)+"</a> "
        if notlast == True:
            nextpage = int(page) + 1
            outstring += " <a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>Next</a>"
            outstring += " <a href='"
            outstring += "/file_selector?type="+type+"&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
            outstring += "'>>></a>"
    else:
        outstring += "no data!"

    if type == "downloads":
        return outstring+"<br /><br /><a href='/fileuploadform'>file upload</a>"
    else:
        return outstring+"<br /><br /><a href='/imageuploadform'>image upload</a>"
#@+node:cmsxh.20131226100304.3679: ** downloadselect_access_list
def downloadselect_access_list(files, starti, endi):
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileSize = os.path.getsize(download_root_dir+"/downloads/"+files[index])
        outstring += '''<input type="checkbox" name="filename" value="'''+files[index]+'''"><a href="#" onclick='window.setLink("/download/?filepath='''+ \
        download_root_dir.replace('\\', '/')+'''/downloads/'''+files[index]+'''",0); return false;'>'''+ \
        files[index]+'''</a> ('''+str(sizeof_fmt(fileSize))+''')<br />'''
    return outstring
#@+node:cmsxh.20131226100304.3680: ** imageselect_access_list
def imageselect_access_list(files, starti, endi):
    outstring = '''<head>
<style>
a.xhfbfile {padding: 0 2px 0 0; line-height: 1em;}
a.xhfbfile img{border: none; margin: 6px;}
a.xhfbfile span{display: none;}
a.xhfbfile:hover span{
    display: block;
    position: relative;
    left: 150px;
    border: #aaa 1px solid;
    padding: 2px;
    background-color: #ddd;
}
a.xhfbfile:hover{
    background-color: #ccc;
    opacity: .9;
    cursor:pointer;
}
</style>
</head>
'''
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileSize = os.path.getsize(download_root_dir+"/images/"+files[index])
        outstring += '''<a class="xhfbfile" href="#" onclick='window.setLink("/download/?filepath='''+ \
        download_root_dir.replace('\\', '/')+'''/images/'''+files[index]+'''",0); return false;'>'''+ \
        files[index]+'''<span style="position: absolute; z-index: 4;"><br />
        <img src="/download/?filepath='''+ \
        download_root_dir.replace('\\', '/')+'''/images/'''+files[index]+'''" width="150px"/></span></a> ('''+str(sizeof_fmt(fileSize))+''')<br />'''
    return outstring
#@+node:cmsxh.20131226100304.3681: ** sizeof_fmt
def sizeof_fmt(num):
    for x in ['bytes','kb','mb','gb']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return "%3.1f %s" % (num, 'tb')
#@+node:cmsxh.20131226100304.3682: ** class CMSimply
class CMSimply(object):
    _cp_config = {
    # if there is no utf-8 encoding, no Chinese input available
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    'tools.sessions.locking' : 'explicit',
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session timeout is 60 minutes
    'tools.sessions.timeout' : 60
    }
    
    #@+others
    #@+node:cmsxh.20140211204322.1703: *3* __init__
    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(download_root_dir+"downloads"):
            try:
                os.makedirs(download_root_dir+"downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"images"):
            try:
                os.makedirs(download_root_dir+"images")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"tmp"):
            try:
                os.makedirs(download_root_dir+"tmp")
            except:
                print("mkdir error")

    #@+node:cmsxh.20131226100304.3683: *3* index
    @cherrypy.expose
    def index(self, heading=None, *args, **kwargs):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        if heading == None:
            heading = head[0]
        page_order = head.index(heading)
        if page_order == 0:
            last_page = ""
        else:
            last_page = head[page_order-1]+" << <a href='get_page?heading="+head[page_order-1]+"'>Previous</a>"
        if page_order == len(head) - 1:
            # no next page
            next_page = ""
        else:
            next_page = "<a href='get_page?heading="+head[page_order+1]+"'>Next</a> >> "+ head[page_order+1]
        if heading == None:
            #  while there is no content in content.htm
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section>"+last_page+" "+next_page+"<br /><h1>"+head[0]+"</h1>"+search_content(head, page, head[0])+"<br />"+last_page+" "+next_page+"</section></div></body></html>"
        else:
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section>"+last_page+" "+next_page+"<br /><h1>"+heading+"</h1>"+search_content(head, page, heading)+"<br />"+last_page+" "+next_page+"</section></div></body></html>"


    #@+node:cmsxh.20131226100304.3684: *3* default
    # default method, if there is no corresponding method, cherrypy will redirect to default method
    # need *args and **kwargs as input variables for all possible URL links
    @cherrypy.expose
    def default_void(self, attr='default', *args, **kwargs):
        raise cherrypy.HTTPRedirect("/")
    #@+node:cmsxh.20131230000041.1602: *3* error_log
    @cherrypy.expose
    def error_log(self, info="Error"):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>ERROR</h1>"+info+"</section></div></body></html>"
    #@+node:cmsxh.20131226100304.3685: *3* login
    @cherrypy.expose
    def login(self):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        if not self.isAdmin():
            return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>Login</h1><form method='post' action='checkLogin'> \
        Password:<input type='password' name='password'> \
        <input type='submit' value='login'></form> \
        </section></div></body></html>"
        else:
            raise cherrypy.HTTPRedirect("/edit_page")
    #@+node:cmsxh.20131226100304.3686: *3* logout
    @cherrypy.expose
    def logout(self):
        cherrypy.session.delete()
        raise cherrypy.HTTPRedirect("/")
    #@+node:cmsxh.20131226100304.3687: *3* checkLogin
    @cherrypy.expose
    def checkLogin(self, password=None):
        site_title, saved_password = parse_config()
        hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        if hashed_password == saved_password:
            cherrypy.session['admin'] = 1
            raise cherrypy.HTTPRedirect("/edit_page")
        raise cherrypy.HTTPRedirect("/")
    #@+node:cmsxh.20131226100304.3688: *3* get_page
    # seperate page need heading and edit variables, if edit=1, system will enter edit mode
    # single page edit will use ssavePage to save content, it means seperate save page
    @cherrypy.expose
    def get_page(self, heading=None, edit=0, *args, **kwargs):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        try:
            pagecontent = search_content(head, page, heading)
            page_order = head.index(heading)
        except:
            heading = head[0]
            pagecontent = page[0]
            page_order = 0
        if page_order == 0:
            # no last page
            last_page = ""
        else:
            last_page = head[page_order-1] + " << <a href='get_page?heading="+head[page_order-1]+"'>Previous</a>"
        if page_order == len(head) - 1:
            # no next page
            next_page = ""
        else:
            next_page = "<a href='get_page?heading="+head[page_order+1]+"'>Next</a> >> "+ head[page_order+1]
        
        # edit=0 for viewpage
        if edit == 0:
            if heading == None:
                return page[0]
            else:
                return self.set_css()+"<div class='container'><nav>"+ \
                directory+"</nav><section>"+last_page+" "+next_page+"<br /><h1>"+heading+"</h1>"+pagecontent+"<br />"+last_page+" "+next_page+"</section></div></body></html>"
        # enter edit mode
        else:
            # check if administrator
            if not self.isAdmin():
                raise cherrypy.HTTPRedirect("/login")
            else:
                pagedata = "<h"+level[page_order]+">"+heading+"</h"+level[page_order]+">"+search_content(head, page, heading)
                outstring = last_page+" "+next_page+"<br />"+ tinymce_editor(directory, cgi.escape(pagedata), page_order)
                return outstring
    #@+node:cmsxh.20131226100304.3689: *3* isAdmin
    def isAdmin(self):
        if cherrypy.session.get('admin') == 1:
            return True
        else:
            return False
    #@+node:cmsxh.20131226100304.3690: *3* edit_page
    # edit all page content
    @cherrypy.expose
    def edit_page(self):
        # check if administrator
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        else:
            head, level, page = parse_content()
            directory = render_menu(head, level, page)
            pagedata =file_get_contents(data_dir+"content.htm")
            outstring = tinymce_editor(directory, cgi.escape(pagedata))
            return outstring
    #@+node:cmsxh.20131226100304.3691: *3* savePage
    @cherrypy.expose
    def savePage(self, page_content=None):
        # check if administrator
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        if page_content == None:
            return self.error_log("no content to save!")
        # we need to check if page heading is redundant
        file = open(data_dir+"content.htm", "w", encoding="utf-8")
        # in Windows client operator, to avoid textarea add extra \n
        page_content = page_content.replace("\n","")
        file.write(page_content)
        file.close()
        raise cherrypy.HTTPRedirect("/edit_page")
    #@+node:cmsxh.20131226100304.3692: *3* ssavePage
    # seperate save page
    @cherrypy.expose
    def ssavePage(self, page_content=None, page_order=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        if page_content == None:
            return self.error_log("no content to save!")
        page_content = page_content.replace("\n","")
        head, level, page = parse_content()
        file = open(data_dir+"content.htm", "w", encoding="utf-8")
        for index in range(len(head)):
            if index == int(page_order):
                file.write(page_content)
            else:
                file.write("<h"+str(level[index])+">"+str(head[index])+"</h"+str(level[index])+">"+str(page[index]))
        file.close()
        # go back to origin edit status
        edit_url = "/get_page?heading="+urllib.parse.quote_plus(head[int(page_order)])+"&edit=1"
        raise cherrypy.HTTPRedirect(edit_url)
    #@+node:cmsxh.20131226100304.3694: *3* fileuploadform
    @cherrypy.expose
    def fileuploadform(self):
        if self.isAdmin():
            head, level, page = parse_content()
            directory = render_menu(head, level, page)
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>file upload</h1>"+'''
<script src="/static/jquery.js" type="text/javascript"></script>
<script src="/static/axuploader.js" type="text/javascript"></script>
<script>
$(document).ready(function(){
$('.prova').axuploader({url:'/fileaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl'],
finish:function(x,files)
        {
            alert('All files have been uploaded: '+files);
        },
enable:true,
remotePath:function(){
  return 'downloads/';
}
});
});
</script>
<div class="prova"></div>
<input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
<input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
</section></body></html>
'''
        else:
            raise cherrypy.HTTPRedirect("/login")
    #@+node:cmsxh.20131226100304.3695: *3* fileaxupload
    @cherrypy.expose
    def fileaxupload(self, *args, **kwargs):
        if self.isAdmin():
            filename = kwargs["ax-file-name"]
            flag = kwargs["start"]
            if flag == 0:
                file = open(download_root_dir+"downloads/"+filename, "wb")
            else:
                file = open(download_root_dir+"downloads/"+filename, "ab")
            file.write(cherrypy.request.body.read())
            file.close()
            return "files uploaded!"
        else:
            raise cherrypy.HTTPRedirect("/login")
    #@+node:cmsxh.20140101145643.3406: *3* flvplayer
    @cherrypy.expose
    def flvplayer(self, filepath=None):
        outstring = '''
    <object type="application/x-shockwave-flash" data="/static/player_flv_multi.swf" width="320" height="240">
         <param name="movie" value="player_flv_multi.swf" />
         <param name="allowFullScreen" value="true" />
         <param name="FlashVars" value="flv='''+filepath+'''&amp;width=320&amp;height=240&amp;showstop=1&amp;showvolume=1&amp;showtime=1
         &amp;startimage=/static/startimage_en.jpg&amp;showfullscreen=1&amp;bgcolor1=189ca8&amp;bgcolor2=085c68
         &amp;playercolor=085c68" />
    </object>
    '''
        return outstring
    #@+node:cmsxh.20131226100304.3696: *3* imageuploadform
    @cherrypy.expose
    def imageuploadform(self):
        if self.isAdmin():
            head, level, page = parse_content()
            directory = render_menu(head, level, page)
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>image upload</h1>"+'''
<script src="/static/jquery.js" type="text/javascript"></script>
<script src="/static/axuploader.js" type="text/javascript"></script>
<script>
$(document).ready(function(){
$('.prova').axuploader({url:'/imageaxupload', allowExt:['jpg','png','gif'],
finish:function(x,files)
        {
            alert('All files have been uploaded: '+files);
        },
enable:true,
remotePath:function(){
  return 'images/';
}
});
});
</script>
<div class="prova"></div>
<input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
<input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
'''
        else:
            raise cherrypy.HTTPRedirect("/login")
    #@+node:cmsxh.20131226100304.3697: *3* imageaxupload
    @cherrypy.expose
    def imageaxupload(self, *args, **kwargs):
        if self.isAdmin():
            filename = kwargs["ax-file-name"]
            flag = kwargs["start"]
            if flag == 0:
                file = open(download_root_dir+"images/"+filename, "wb")
            else:
                file = open(download_root_dir+"images/"+filename, "ab")
            file.write(cherrypy.request.body.read())
            file.close()
            return "image files uploaded!"
        else:
            raise cherrypy.HTTPRedirect("/login")
    #@+node:cmsxh.20131226100304.3698: *3* file_selector
    @cherrypy.expose
    def file_selector(self, type=None, page=1, item_per_page=10, keyword=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        else:
            if type == "downloads":
                #return downloads_file_selector()
                return file_lister("downloads", type, page, item_per_page)
            elif type == "image":
                #return images_file_selector()
                return file_lister("images", type, page, item_per_page)
    #@+node:cmsxh.20131226100304.3699: *3* download_list
    @cherrypy.expose
    def download_list(self, item_per_page=5, page=1, keyword=None, *args, **kwargs):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        # cherrypy.session['admin'] = 1
        # cherrypy.session.get('admin')
        files = os.listdir(download_root_dir+"downloads/")
        total_rows = len(files)
        totalpage = math.ceil(total_rows/int(item_per_page))
        starti = int(item_per_page) * (int(page) - 1) + 1
        endi = starti + int(item_per_page) - 1
        outstring = "<form method='post' action='delete_file'>"
        notlast = False
        if total_rows > 0:
            outstring += "<br />"
            if (int(page) * int(item_per_page)) < total_rows:
                notlast = True
            if int(page) > 1:
                outstring += "<a href='"
                outstring += "/download_list?&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'><<</a> "
                page_num = int(page) - 1
                outstring += "<a href='"
                outstring += "/download_list?&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Previous</a> "
            span = 10
            for index in range(int(page)-span, int(page)+span):
                if index>= 0 and index< totalpage:
                    page_now = index + 1 
                    if page_now == int(page):
                        outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                    else:
                        outstring += "<a href='"
                        outstring += "/download_list?&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                        outstring += "'>"+str(page_now)+"</a> "

            if notlast == True:
                nextpage = int(page) + 1
                outstring += " <a href='"
                outstring += "/download_list?&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Next</a>"
                outstring += " <a href='"
                outstring += "/download_list?&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>>></a><br /><br />"
            if (int(page) * int(item_per_page)) < total_rows:
                notlast = True
                outstring += downloadlist_access_list(files, starti, endi)+"<br />"
            else:
                outstring += "<br /><br />"
                outstring += downloadlist_access_list(files, starti, total_rows)+"<br />"
            
            if int(page) > 1:
                outstring += "<a href='"
                outstring += "/download_list?&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'><<</a> "
                page_num = int(page) - 1
                outstring += "<a href='"
                outstring += "/download_list?&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Previous</a> "
            span = 10
            for index in range(int(page)-span, int(page)+span):
            #for ($j=$page-$range;$j<$page+$range;$j++)
                if index >=0 and index < totalpage:
                    page_now = index + 1
                    if page_now == int(page):
                        outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                    else:
                        outstring += "<a href='"
                        outstring += "/download_list?&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                        outstring += "'>"+str(page_now)+"</a> "
            if notlast == True:
                nextpage = int(page) + 1
                outstring += " <a href='"
                outstring += "/download_list?&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Next</a>"
                outstring += " <a href='"
                outstring += "/download_list?&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>>></a>"
        else:
            outstring += "no data!"
        outstring += "<br /><br /><input type='submit' value='delete'><input type='reset' value='reset'></form>"

        head, level, page = parse_content()
        directory = render_menu(head, level, page)

        return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Download List</h1>"+outstring+"<br/><br /></body></html>"
    #@+node:cmsxh.20131226100304.5427: *3* delete_file
    @cherrypy.expose
    def delete_file(self, filename=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        if filename == None:
            outstring = "no file selected!"
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Delete Error</h1>"+outstring+"<br/><br /></body></html>"
        outstring = "delete all these files?<br /><br />"
        outstring += "<form method='post' action='doDelete'>"
        # only one file is selected
        if isinstance(filename, str):
            outstring += filename+"<input type='hidden' name='filename' value='"+filename+"'><br />"
        else:
            # multiple files selected
            for index in range(len(filename)):
                outstring += filename[index]+"<input type='hidden' name='filename' value='"+filename[index]+"'><br />"
        outstring += "<br /><input type='submit' value='delete'></form>"

        return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Download List</h1>"+outstring+"<br/><br /></body></html>"
    #@+node:cmsxh.20131226100304.5428: *3* doDelete
    @cherrypy.expose
    def doDelete(self, filename=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        # delete files
        outstring = "all these files will be deleted:<br /><br />"
        # only select one file
        if isinstance(filename, str):
            try:
                os.remove(download_root_dir+"downloads/"+filename)
                outstring += filename+" deleted!"
            except:
                outstring += filename+"Error, can not delete files!<br />"
        else:
            # multiple files selected
            for index in range(len(filename)):
                try:
                    os.remove(download_root_dir+"downloads/"+filename[index])
                    outstring += filename[index]+" deleted!<br />"
                except:
                    outstring += filename[index]+"Error, can not delete files!<br />"

        head, level, page = parse_content()
        directory = render_menu(head, level, page)

        return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Download List</h1>"+outstring+"<br/><br /></body></html>"
    #@+node:cmsxh.20131226100304.3700: *3* creo_getvolume
    @cherrypy.expose
    def creo_getvolume(self, *args, **kwargs):
        return '''
<script src="/static/weblink/pfcUtils.js">
</script><script  src="/static/weblink/pfcParameterExamples.js"></script><script  src="/static/weblink/pfcComponentFeatExamples.js">
 document.writeln ("Error loading script!");
</script><script language="JavaScript">
    if (!pfcIsWindows())
        netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
  var session = pfcGetProESession ();
// for volume
  var solid = session.CurrentModel;
    try
        {
            createParametersFromArguments ();
            solid.Regenerate(void null);   
            properties = solid.GetMassProperty(void null);
            alert("part volume:"+properties.Volume);
        }
    catch (err)
        {
            alert ("Exception occurred: "+pfcGetExceptionType (err));
       }
</script>
'''
    #@+node:cmsxh.20131226100304.3701: *3* anglebracket
    @cherrypy.expose
    def anglebracket(self, *args, **kwargs):
        return '''
<script src="/static/weblink/pfcUtils.js">
</script><script src="/static/weblink/wl_header.js">
document.writeln ("Error loading Pro/Web.Link header!");
</script><script language="JavaScript">
if (!pfcIsWindows()) netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
// if the third input is false, it means use session, but will not be displayed
// ret is the model open return
 var ret = document.pwl.pwlMdlOpen("angle_bracket_creo.prt", "c:/tmp", false);
if (!ret.Status) {
    alert("pwlMdlOpen failed (" + ret.ErrorCode + ")");
}
    var session = pfcGetProESession();
    var window = session.OpenFile(pfcCreate("pfcModelDescriptor").CreateFromFileName("angle_bracket_creo.prt"));
    var solid = session.GetModel("angle_bracket_creo.prt",pfcCreate("pfcModelType").MDL_PART);
    var d1,d2,myf,myn,i,j,volume,count,d1Value,d2Value;
    d1 = solid.GetParam("len1");
    //d2 = solid.GetParam("width");
    //myf=20;
    //myn=20;
    volume=0;
    count=0;
    try
    {
            //createParametersFromArguments ();
            for(i=0;i<=3;i++)
            {
                //for(j=0;j<=2;j++)
                //{
                    myf=180+i;
                    //myn=100+i*10;
         d1Value = pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myf);
         d2Value = pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myn);
                    d1.Value = d1Value;
                    //d2.Value = d2Value;
                    solid.Regenerate(void null);
                    properties = solid.GetMassProperty(void null);
                    //volume = volume + properties.Volume;
volume = properties.Volume;
                    count = count + 1;
alert("execute no: "+count+", part volume:"+volume);
var newfile = document.pwl.pwlMdlSaveAs("angle_bracket_creo.prt", "c:/tmp", "cadp_w12_py_"+count+".prt");
if (!newfile.Status) {
    alert("pwlMdlSaveAs failed (" + newfile.ErrorCode + ")");
//}
                }
            }
            //alert("totally execute:"+count+"times, part volume:"+volume);
            //alert("part volume:"+properties.Volume);
            //alert("part volume to integer:"+Math.round(properties.Volume));
        }
    catch(err)
        {
            alert ("Exception occurred: "+pfcGetExceptionType (err));
        }
</script>
'''
    #@+node:cmsxh.20131226100304.3702: *3* search_form
    @cherrypy.expose
    def search_form(self):
        if self.isAdmin():
            head, level, page = parse_content()
            directory = render_menu(head, level, page)
            return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>Search</h1><form method='post' action='doSearch'> \
        keywords:<input type='text' name='keyword'> \
        <input type='submit' value='search'></form> \
        </section></div></body></html>"
        else:
            raise cherrypy.HTTPRedirect("/login")
    #@+node:cmsxh.20131226100304.3703: *3* doSearch
    @cherrypy.expose
    def doSearch(self, keyword=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        else:
            head, level, page = parse_content()
            directory = render_menu(head, level, page)
            match = ""
            for index in range(len(head)):
                if keyword != "" and (keyword.lower() in page[index].lower() or \
                keyword.lower() in head[index].lower()): \
                    match += "<a href='/get_page?heading="+head[index]+"'>"+head[index]+"</a><br />"
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Search Result</h1>keyword: "+ \
            keyword.lower()+"<br /><br />in the following pages:<br /><br />"+ \
            match+" \
         </section></div></body></html>"
    #@+node:cmsxh.20131226100304.3704: *3* set_css
    def set_css(self):
        outstring = '''<!doctype html><html><head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <title>CMSimply - Simple Cloud CMS in Python 3</title> \
    <link rel="stylesheet" type="text/css" href="/static/cmsimply.css">
    '''+syntaxhighlight()

        outstring += '''
    <script src="/static/jquery.js"></script>
    <script type="text/javascript">
    $(function(){
        $("ul.topmenu> li:has(ul) > a").append('<div class="arrow-right"></div>');
        $("ul.topmenu > li ul li:has(ul) > a").append('<div class="arrow-right"></div>');
    });
    </script>
    '''
        if inOpenshift:
            outstring += '''
    <script type="text/javascript">
    if ((location.href.search(/http:/) != -1) && (location.href.search(/login/) != -1)) \
    window.location= 'https://' + location.host + location.pathname + location.search;
    </script>
    '''
        site_title, password = parse_config()
        outstring += '''
    </head><header><h1>'''+site_title+'''</h1> \
    <confmenu>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/sitemap">Site Map</a></li>
    '''
        if self.isAdmin():
            outstring += '''
    <li><a href="/edit_page">Edit All</a></li>
    <li><a href="'''+cherrypy.url(qs=cherrypy.request.query_string)+'''&edit=1">Edit</a></li>
    <li><a href="/edit_config">Config</a></li>
    <li><a href="/search_form">Search</a></li>
    <li><a href="/imageuploadform">image upload</a></li>
    <li><a href="/fileuploadform">file upload</a></li>
    <li><a href="/download_list">file list</a></li>
    <li><a href="/logout">logout</a></li>
    '''
        else:
            outstring += '''
    <li><a href="/login">login</a></li>
    '''
        outstring += '''
    </ul>
    </confmenu></header>
    '''
        return outstring
    #@+node:cmsxh.20131226100304.3705: *3* edit_config
    @cherrypy.expose
    def edit_config(self):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        if not self.isAdmin():
            return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>Login</h1><form method='post' action='checkLogin'> \
        Password:<input type='password' name='password'> \
        <input type='submit' value='login'></form> \
        </section></div></body></html>"
        else:
            site_title, password = parse_config()
            # edit config file
            return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>Edit Config</h1><form method='post' action='saveConfig'> \
        Site Title:<input type='text' name='site_title' value='"+site_title+"' size='50'><br /> \
        Password:<input type='text' name='password' value='"+password+"' size='50'><br /> \
     <input type='hidden' name='password2' value='"+password+"'> \
        <input type='submit' value='send'></form> \
        </section></div></body></html>"
    #@+node:cmsxh.20131226100304.3706: *3* saveConfig
    @cherrypy.expose
    def saveConfig(self, site_title=None, password=None, password2=None):
        if not self.isAdmin():
            raise cherrypy.HTTPRedirect("/login")
        if site_title == None or password == None:
            return self.error_log("no content to save!")
        old_site_title, old_password = parse_config()
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        if site_title == None or password == None or password2 != old_password or password == '':
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>Error!</h1><a href='/'>Home</a></body></html>"
        else:
            if password == password2 and password == old_password:
                hashed_password = old_password
            else:
                hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
            file = open(data_dir+"config", "w", encoding="utf-8")
            file.write("siteTitle:"+site_title+"\npassword:"+hashed_password)
            file.close()
            return self.set_css()+"<div class='container'><nav>"+ \
            directory+"</nav><section><h1>config file saved</h1><a href='/'>Home</a></body></html>"
    #@+node:cmsxh.20131226100304.3707: *3* listdir
    # use to check directory variable data
    @cherrypy.expose
    def listdir(self):
        return download_root_dir +","+data_dir
    #@+node:cmsxh.20131226100304.3708: *3* sitemap
    @cherrypy.expose
    def sitemap(self):
        head, level, page = parse_content()
        directory = render_menu(head, level, page)
        sitemap = render_menu(head, level, page, sitemap=1)

        return self.set_css()+"<div class='container'><nav>"+ \
        directory+"</nav><section><h1>Site Map</h1>"+sitemap+"</section></div></body></html>"
    #@+node:2014pythonE.20140312072052.1941: *3* brython
    @cherrypy.expose
    def brython(self):
        return '''
    <!doctype html>
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <link rel="stylesheet" type="text/css" href="/static/console.css">
    <link rel="stylesheet" type="text/css" href="/static/brython.css">
    <script type="text/javascript" src="/static/Brython2.0.0-20140209-164925/brython.js"></script>
    <script type="text/javascript">
    window.onload = function(){
        brython({debug:0, cache:'none'});
    };
    </script>

    <script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript">
    </script>

    <script type="text/python3" src="/static/editor.py"></script>

    <script type="text/python3">
    from browser import doc

    # other translations

    trans = {
        'report_bugs':{'en':'Please report bugs in the ',
                       'es':'Poner los bugs en el ',
                       'fr':"Signalez les bugs dans l'"},
        'test_page':{'en':'Tests page','es':'P&aacute;gina de pruebas','fr':'Page de tests'},
        'run':{'en':'run','es':'ejecutar','fr':'exécuter'},
        'clear':{'en':'clear','es':'borrar','fr':'effacer'}
    }

    for key in trans:
        if key in doc:
            doc[key].html = trans[key].get(language,trans[key]['en'])

    def set_debug(ev):
        if ev.target.checked:
            __BRYTHON__.debug = 1
        else:
            __BRYTHON__.debug = 0

    # bindings
    doc['run_js'].bind('click',run_js)
    doc['set_debug'].bind('change',set_debug)

    # next functions are defined in editor.py
    doc['show_js'].bind('click',show_js)
    doc['run'].bind('click',run)
    doc['show_console'].bind('click',show_console)
    doc['reset_the_src'].bind('click',reset_the_src)
    doc['clear_console'].bind('click',clear_console)
    doc['clear_src'].bind('click',clear_src)
    </script>

    <script>
    function run_js(){
        var cons = document.getElementById("console")
        var jscode = cons.value
        var t0 = (new Date()).getTime()
        eval(jscode)
        var t1 = (new Date()).getTime()
        console.log("Javascript code run in "+(t1-t0)+" ms")
    }
    </script>
    </head>
    <body>
    <!--<body onload="brython({debug:1, cache:'version'})">-->

    <div style="text-align:center">
    <br>Brython version: <span id="version"></span>
    </div>
    </center>

    <div id="container">
    <div id="left-div">
    <div style="padding: 3px 3px 3px 3px;">
    Theme: <select id="ace_theme">
    <optgroup label="Bright">
    <option value="ace/theme/chrome">Chrome</option>
    <option value="ace/theme/clouds">Clouds</option>
    <option value="ace/theme/crimson_editor">Crimson Editor</option>
    <option value="ace/theme/dawn">Dawn</option>
    <option value="ace/theme/dreamweaver">Dreamweaver</option>
    <option value="ace/theme/eclipse">Eclipse</option>
    <option value="ace/theme/github">GitHub</option>
    <option value="ace/theme/solarized_light">Solarized Light</option>
    <option value="ace/theme/textmate">TextMate</option>
    <option value="ace/theme/tomorrow">Tomorrow</option>
    </optgroup>
    <optgroup label="Dark">
    <option value="ace/theme/clouds_midnight">Clouds Midnight</option>
    <option value="ace/theme/cobalt">Cobalt</option>
    <option value="ace/theme/idle_fingers">idleFingers</option>
    <option value="ace/theme/merbivore">Merbivore</option>
    <option value="ace/theme/merbivore_soft">Merbivore Soft</option>
    <option value="ace/theme/mono_industrial">Mono Industrial</option>
    <option value="ace/theme/monokai">Monokai</option>
    <option value="ace/theme/pastel_on_dark">Pastel on dark</option>
    <option value="ace/theme/solarized_dark">Solarized Dark</option>
    <option value="ace/theme/twilight">Twilight</option>
    <option value="ace/theme/tomorrow_night">Tomorrow Night</option>
    <option value="ace/theme/tomorrow_night_blue">Tomorrow Night Blue</option>
    <option value="ace/theme/tomorrow_night_bright">Tomorrow Night Bright</option>
    <option value="ace/theme/tomorrow_night_eighties">Tomorrow Night 80s</option>
    <option value="ace/theme/vibrant_ink">Vibrant Ink</option>
    </optgroup>
    </select> 
    </div>
      <div id="editor" style="height: 400px; width: 500px"></div>
    </div>

    <div>
        <button id="reset_the_src">reset the_src</button>
        <button id="clear_src">clear src</button>
        <button id="clear_console">clear console</button>
    </div>

    <div id="right-div">
    <div style="padding: 3px 3px 3px 3px;">
      <div style="float:left">
        <button id="run">run</button>
        <button id="run_js">run Javascript</button>
        debug<input type="checkbox" id="set_debug" checked>
      </div>

      <div style="float:right">
        <button id="show_console">Console</button>
        <button id="show_js">Javascript</button>
      </div>
    </div>
    <div style="width:100%;height:100%;">
    <textarea id="console" style="height: 380px; width: 500px"></textarea>
    </div>
    </div>
    </body>
    </html>
    '''
    #@-others
#@+node:cmsxh.20131226100304.3709: ** class Download
class Download:
    #@+others
    #@+node:cmsxh.20131226100304.3710: *3* index
    @cherrypy.expose
    def index(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")
    #@-others
#@-others
root = CMSimply()
root.download = Download()

# setup static, images and downloads directories
application_conf = {'/static':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': _curdir+"/static"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"}
    }

# if inOpenshift ('OPENSHIFT_REPO_DIR' exists in environment variables) or not inOpenshift
if inOpenshift:
    # operate in OpenShift
    application = cherrypy.Application(root, config = application_conf)
else:
    # operate in localhost
    cherrypy.quickstart(root, config = application_conf)
#@-leo
