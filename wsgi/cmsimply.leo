<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo (http://leoeditor.com/leo_toc.html) -->
<?xml-stylesheet ekr_test?>
<leo_file xmlns:leo="http://www.leo-editor.org/2011/leo" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="cmsxh.20131226100304.5349" a="E"><vh>@settings</vh>
<v t="cmsxh.20131226100304.5350"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="cmsxh.20131226100304.5351"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="cmsxh.20140108172857.2428"><vh>CMSimply public version</vh></v>
<v t="cmsxh.20131226100304.3770" a="E"><vh>CMSimply Project</vh>
<v t="cmsxh.20140101145643.1604"><vh>License</vh></v>
<v t="cmsxh.20131226100304.5424"><vh>Delete uploaded files</vh></v>
<v t="cmsxh.20131226100304.5425"><vh>View uploaded files</vh></v>
<v t="cmsxh.20140212132226.1611"><vh>View uploaded images</vh></v>
<v t="cmsxh.20140212132226.1612"><vh>Delete tmp session files</vh></v>
<v t="cmsxh.20131226100304.5426"><vh>about textile</vh></v>
<v t="2014pythonE.20140312072052.1942"><vh>about syntaxhighlight</vh></v>
<v t="2014pythonE.20140313091306.1898"><vh>Brython ajax</vh></v>
<v t="2014pythonE.20140313212213.1898" a="E"><vh>CherryPy ajax example</vh>
<v t="2014pythonE.20140313212213.1899"><vh>another example</vh></v>
<v t="2014pythonE.20140313212213.1902"><vh>reference site</vh></v>
<v t="2014pythonE.20140313212213.1900" a="E"><vh>localStorage</vh>
<v t="2014pythonE.20140313212213.1901"><vh>example</vh></v>
</v>
</v>
<v t="cmsxh.20140212132226.1610"><vh>Error</vh></v>
</v>
<v t="cmsxh.20131226100304.3660" a="E"><vh>@path ./</vh>
<v t="cmsxh.20131226100304.3661" a="E"
expanded="cmsxh.20131226100304.3682,cmsxh.20131226100304.3709,"><vh>@file application</vh></v>
<v t="cmsxh.20131226100304.3823"><vh>@edit .gitignore</vh></v>
<v t="cmsxh.20131226100304.3820" a="E"><vh>@path static</vh>
<v t="cmsxh.20131226100304.3821"><vh>@edit cmsimply.css</vh></v>
<v t="cmsxh.20131226100304.3822"><vh>@edit axuploader.js</vh></v>
<v t="2014pythonE.20140312215910.1786"><vh>@edit console.css</vh></v>
<v t="2014pythonE.20140312215910.1787"><vh>@edit brython.css</vh></v>
<v t="2014pythonE.20140312215910.1788"><vh>@edit editor.py</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="2014pythonE.20140312072052.1942">At this moment, the syntaxhighlight cause the Brython error.
When syntaxhighlight return anything but None, error arises.

It is believed that the CherryPy header cause this problem.

According to: http://stackoverflow.com/questions/6054473/python-cherrypy-how-to-add-header

"When you set a status code by raising HTTPError, the headers in cherrypy.response.headers are ignored. Set the HTTP status by setting cherrypy.response.status instead:"

add the following lines into index() to eliminate this problem:

# Yen try
cherrypy.response.headers['Retry-After'] = 60
cherrypy.response.status = 404

According to: http://cherrypy.readthedocs.org/en/latest/tutorial/basics.html

Since "cherrypy.response.headers contains a mapping with the header options that will be returned by the server, before the contents get sent."

The real problem comes from default(), while the CMSimply class operated normally, the default() sent some header message to cause brython not working.

The syntaxhighlight is not the problem anymore.
</t>
<t tx="2014pythonE.20140313091306.1898">&lt;div id="result"&gt;(empty)&lt;/div&gt;
&lt;button id="get_text"&gt;get text file&lt;/button&gt;
&lt;button id="i_dont_exist"&gt;file not found&lt;/button&gt;
&lt;button id="get_test"&gt;GET request&lt;/button&gt;
&lt;button id="post_test"&gt;POST request&lt;/button&gt;
&lt;button id="timeout"&gt;timeout&lt;/button&gt;

&lt;script id="ascript" type="text/python"&gt;
from browser import ajax,doc

def on_complete(req):
    print(req.readyState)
    print('status',req.status)
    if req.status==200 or req.status==0:
        doc["result"].html = req.text
    else:
        doc["result"].html = "error "+req.text

def err_msg():
    doc["result"].html = "server didn't reply after %s seconds" %timeout

timeout = 4

def go(url):
    req = ajax.ajax()
    req.bind('complete',on_complete)
    req.set_timeout(timeout,err_msg)
    req.open('GET',url,True)
    req.send()

def post(url):
    req = ajax.ajax()
    req.bind('complete',on_complete)
    req.set_timeout(timeout,err_msg)
    req.open('POST',url,True)
    req.set_header('content-type','application/x-www-form-urlencoded')
    req.send({'foo':34})

# bindings
doc['get_text'].bind('click',lambda ev:go('ajax_data.txt'))
doc['i_dont_exist'].bind('click',lambda ev:go('i_dont_exist.txt'))
doc['get_test'].bind('click',lambda ev:go('/cgi-bin/get_test.py'))
doc['post_test'].bind('click',lambda ev:post('/cgi-bin/post_test.py'))
doc['timeout'].bind('click',lambda ev:go('/cgi-bin/timeout.py'))
&lt;/script&gt;</t>
<t tx="2014pythonE.20140313212213.1898">import cherrypy
import simplejson

class Root(object):

    @cherrypy.expose
    def update(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = simplejson.loads(rawbody)
        # do_something_with(body)
        return "Updated %r." % (body,)

    @cherrypy.expose
    def index(self):
        return """
&lt;html&gt;
&lt;script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"&gt;&lt;/script&gt;
&lt;script type='text/javascript'&gt;
function Update() {
    $.ajax({
      type: 'POST',
      url: "update",
      contentType: "application/json",
      processData: false,
      data: $('#updatebox').val(),
      success: function(data) {alert(data);},
      dataType: "text"
    });
}
&lt;/script&gt;
&lt;body&gt;
&lt;input type='textbox' id='updatebox' value='{}' size='20' /&gt;
&lt;input type='submit' value='Update' onClick='Update(); return false' /&gt;
&lt;/body&gt;
&lt;/html&gt;
"""

cherrypy.quickstart(Root())</t>
<t tx="2014pythonE.20140313212213.1899">import cherrypy
import simplejson

class Root:

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def my_route(self):

        result = {"operation": "request", "result": "success"}

        input_json = cherrypy.request.json
        value = input_json["my_key"]

        #All responses are serialized to JSON. This the same as
        #return simplejson.dumps(result)
        return result
        
Javascript part:

//assuming that you're using jQuery

var myObject = { "my_key": "my_value" };

$.ajax({
    type: "POST",
    url: "my_route",
    data: JSON.stringify(myObject),
    contentType: 'application/json',
    dataType: 'json',
    error: function() {
        alert("error");
    },
    success: function() {
        alert("success");
    }
});</t>
<t tx="2014pythonE.20140313212213.1900">localStorage:

存值：
localStorage.setItem(key,value);

取值：
localStorage.getItem(key);

移除KEY所對應的內容:
localStorage.removeItem(key);

清除所有內容
localStorage.clear();

&lt;script&gt;
    // set an item
    localStorage.setItem('name','goofy');
    // retrieve an item
    alert(localStorage.getItem('name'));
    // empty the localStorage completely
    localStorage.clear();
&lt;/script&gt;

&lt;script "text/javascript"&gt;
    start = new Date().getTime();
    for(i=1;i&lt;=1000;i++)
        localStorage.setItem(i.toString(),'a' * 1024);
    elapsed = ((new Date().getTime()) - start)/1000
    alert(elapsed.toString() + "s");
&lt;/script&gt;

&lt;script&gt;
    for(i=0; i&lt;localStorage.length; i++) {
        key = localStorage.key(i);
        item = localStorage.getItem(key);
        // do something with key and item ...
    }
&lt;/script&gt;</t>
<t tx="2014pythonE.20140313212213.1901">example: http://dreamforce.me/wp-content/dream_demo/html5_localstorage/html5_localDemo/html5_localstorage.html

&lt;!DOCTYPE html&gt; 
&lt;head&gt; 
	&lt;meta http-equiv="content-type" content="text/html; charset=UTF-8"/&gt; 
	&lt;title&gt;Cute Bar Demo - SpyreStudios&lt;/title&gt; 
	&lt;script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.js'&gt;&lt;/script&gt; 
	&lt;script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.js'&gt;&lt;/script&gt; 
	&lt;script type='text/javascript' src='js/jquery.dataTables.js'&gt;&lt;/script&gt; 
	
	&lt;link href="css/jquery.ui.all.css" rel="stylesheet" type="text/css" media="all"/&gt;
	
	&lt;link href="css/demo_page.css" rel="stylesheet" type="text/css" media="all"/&gt;
	&lt;link href="css/demo_table_jui.css" rel="stylesheet" type="text/css" media="all"/&gt;
	&lt;link href="css/demo_table.css" rel="stylesheet" type="text/css" media="all"/&gt;
	
	&lt;script type='text/javascript'&gt; 
	var currentId = 1;
	var oTable;
    $(document).ready(function(){    
		if (typeof(localStorage) == 'undefined' ) {
			alert('Your browser does not support HTML5 localStorage. Try upgrading.');
		} else {
		try {
		var currentId = localStorage.getItem("currentId")
		if(currentId == null)
		{
		localStorage.setItem("currentId",1);
		currentId = 1;
		}
		  oTable = $('#localDataList').dataTable({
					"bJQueryUI": true,
					"sPaginationType": "full_numbers"
				});
		    addLocalStorageToTabel();		
		} catch (e) {
	 	 if (e == QUOTA_EXCEEDED_ERR) {
	 	 	 alert('Quota exceeded!'); //data wasn't successfully saved due to quota exceed so throw an error
		}
	    }
       }

    });
	
	function getStoredObjIdsArray()
	{
	   var ids = localStorage.getItem("storedObjIds");
	   var idStrArray;
	   if(ids!=null)
		{
        idStrArray = ids.split(",");
		}
		return idStrArray;
	}
	function addLocalStorageToTabel()
	{
	    oTable.fnClearTable();
	    var ids_Array = getStoredObjIdsArray();
		if(ids_Array!=null)
		{
		for ( var j = 0; j &lt; ids_Array.length; j++) {
		    var theId = ids_Array[j];
			var objStr = localStorage.getItem(theId);
			if(objStr != null)
			{
			   var objField = objStr.split("|");
			   addDataToTable(theId,objField[0],objField[1]);
			}
			}
	}
	}
	
	function addDataToTable(id,name,age)
	{
	  var deleteStr = '&lt;a href="javascript:void(0)" onclick="deleteObjStr('+id+');"&gt;delete&lt;/a&gt;';
	  oTable.fnAddData( [
        id,
		name,
		age,
		deleteStr
		] );
	}
	
	function deleteObjStr(id)
	{
	   var objStr = localStorage.getItem(id);
	   if(objStr!=null)
	   {
	       alert(objStr);
	       alert("in");
	       localStorage.removeItem(id);
		   addLocalStorageToTabel();
	   }
	}
	

	
	function setObjStrTolocalStorage() 
	{
	    var name = $("#nameValue").val();
		if(name==null || name=='')
		{
		  alert("please input name value!");
		  return false;
		}
		var age  = $("#ageValue").val();
		if(age==null || age =='')
		{
		  alert("please input age value!");
		  return false;
		}
		if(isNaN(age))
		{
		  alert("the age value must be int type!");
		  return false;
		}
		var id   = localStorage.getItem("currentId");
		localStorage.setItem(id,name+"|"+age);
		var ids = localStorage.getItem("storedObjIds");
		if(ids!=null)
		{
         ids+=","+id;
		}
		else
		{
		  ids = id;
		}
		localStorage.setItem("storedObjIds",ids);
		
		addCurrentIdPoint();
	}
	
	function addDataToLocalStorage()
	{
	    setObjStrTolocalStorage();
		addLocalStorageToTabel();
		$("#addDataToForm").dialog("close")
	 }
	 
	 function addCurrentIdPoint()
	 {
	   var currentId = localStorage.getItem("currentId");	
	   var currentIdInt = parseInt(currentId) + 1;
	   localStorage.setItem("currentId",currentIdInt);
	 }
	 
	function addDataReady()
	{
	  var id   = localStorage.getItem("currentId");
	  $("#currentIdLabel").html("Current ID: "+id);
	  var target = $("#addDataToForm")
	  setDisplayArea(target)
	  $(target).dialog("open");
	}
	
	function setDisplayArea(target, recall) {
	$(target).dialog({
		autoOpen : false,
		width : "auto",
		height : "auto",
		modal : true,
		position : "center",
		beforeClose : recall
	});
}

	&lt;/script&gt; 

&lt;/head&gt; 
&lt;body&gt; 
   &lt;a href="javascript:void(0)" onclick="addDataReady()"&gt;You can add Data Here!&lt;/a&gt;
   &lt;div id="addDataToForm" style="display:none;"&gt;
   &lt;span id="currentIdLabel"&gt;ID:&lt;/span&gt;&amp;nbsp;&lt;span&gt;Name:&lt;input type="text" id="nameValue"&gt;&lt;/span&gt;&amp;nbsp;&lt;span&gt;Age: &lt;input type="text" id="ageValue"&gt;&lt;/span&gt;&amp;nbsp;&lt;span&gt;&lt;a href="javascript:void(0)" onclick="addDataToLocalStorage();"&gt;ADD&lt;/a&gt;&lt;/span&gt;
   &lt;/div&gt;
   &lt;table id="localDataList" style="border:1px solid; width:100%;"&gt;
     &lt;thead&gt;
     &lt;tr id="head"&gt;
	   &lt;td width="20%"&gt;ID&lt;/td&gt;&lt;td width="20%"&gt;Name&lt;/td&gt;&lt;td width="20%"&gt;Age&lt;/td&gt;&lt;td width="40%"&gt;Operation&lt;/td&gt;
	 &lt;/tr&gt;
	 &lt;/thead&gt;
	 &lt;tbody&gt;
	 &lt;tr&gt;
	   &lt;td&gt;ID&lt;/td&gt;&lt;td&gt;Name&lt;/td&gt;&lt;td&gt;Age&lt;/td&gt;&lt;td&gt;Operation&lt;/td&gt;
	 &lt;/tr&gt;
	 &lt;/tbody&gt;
   &lt;/table&gt;
&lt;/body&gt; 
 
 
&lt;/html&gt; 
</t>
<t tx="2014pythonE.20140313212213.1902">http://ginstrom.com/scribbles/2010/03/07/simple-ajax-with-cherrypy-and-jquery/

minijQyery Lab: http://www.darkthread.net/MiniJQueryLab/
</t>
<t tx="cmsxh.20131226100304.3660"></t>
<t tx="cmsxh.20131226100304.3770">Ultrasimple Content Management System

V. 0.14 - add uploaded files deletion
V. 0.15 - ready for git remote add to bitbucket
V. 0.16 - change language to English</t>
<t tx="cmsxh.20131226100304.3820"></t>
<t tx="cmsxh.20131226100304.5349"></t>
<t tx="cmsxh.20131226100304.5350">QSplitter::handle {
    background-color: #CAE1FF; /* lightSteelBlue1 */
}

QStackedWidget {
    /* background-color:lightpink; */
    border-color: red;
    padding: 0px;
    /* border-width: 0px; */
    /* background-color: yellow; */
}

QSplitter {
    border-color: white;
    background-color: white;
    border-style: solid;
}

QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 22px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="cmsxh.20131226100304.5351">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="cmsxh.20131226100304.5424">Hope to provide a way for multiple files selection and delete

To delete files, double confirmation is needed

Procedure:

1. add html form for download_list method, one seleciton for each file, as well as providing to send to delete confirmation method.

2. confirmation method list all the to be deleted files, and ask for delete confirmation, is yes for deletion, all the listed files will be delete.

3. for safety of data management, all deleted files should be moved to the garbage files to timed final deletion.
</t>
<t tx="cmsxh.20131226100304.5425">The file format allowed for upload:

1. general files, including 7z, zip and pdf files.

2. graphics files, including png, jpg, gif files.

3. video files, including flv files.

4. audio files, including mp3 files.

5. parts files, including stl, Creo part and assembly, Solvespace files, Solid Edge files.</t>
<t tx="cmsxh.20131226100304.5426">textile library are used to generated sitemap and tree menu unordeded list.

Due to the efficiency problem, textile is not used anymore, custom "render_menu" method is used.</t>
<t tx="cmsxh.20140101145643.1604">Copyright © 2014 Chiaming Yen

CMSimply is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CMSimply is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CMSimpiy. If not, see &lt;http://www.gnu.org/licenses/&gt;.</t>
<t tx="cmsxh.20140108172857.2428">version on public-cmsimply.rhcloud.com
</t>
<t tx="cmsxh.20140212132226.1610">1. in SSL mode no arrow for menu - modified to use local jquery.js file

2. Brython editor can not save a 700-line program - it is the mailformated URI problem not the timeout problem.

3. upload file will write on top of the duplicated file, in stead of create a new file. (a bug need to fix)

4. duplicated page title problem need to deal with.



</t>
<t tx="cmsxh.20140212132226.1611">add images directory file list

when administrator press list image file button, system will check if thumb images are exist or not, the list will show thum image file and press to view original image file.

We may also want to delete image files.</t>
<t tx="cmsxh.20140212132226.1612">see if we need to delete all the tmp session files after logout</t>
</tnodes>
</leo_file>
