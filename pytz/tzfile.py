



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "QAxhIW9WGzKiMfpWCuaOQHxnc6o:1354171146555";
 
 
 var CS_env = {"projectName":"compcrimson","loggedInUserEmail":"whhhmarks@gmail.com","profileUrl":"/u/100545230244848929459/","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13882333484250518008","token":"QAxhIW9WGzKiMfpWCuaOQHxnc6o:1354171146555","projectHomeUrl":"/p/compcrimson","relativeBaseUrl":"","assetHostPath":"https://ssl.gstatic.com/codesite/ph","domainName":null};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>tzfile.py - 
 compcrimson -
 
 
 business board comp sheets - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13882333484250518008/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13882333484250518008/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13882333484250518008/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13882333484250518008/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>whhhmarks@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/100545230244848929459/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/100545230244848929459/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fcompcrimson%2Fsource%2Fbrowse%2Fpytz%2Ftzfile.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/compcrimson">
 <a href="/p/compcrimson/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/compcrimson/"><span itemprop="name">compcrimson</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/compcrimson/"><span itemprop="description">business board comp sheets</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/compcrimson/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 <a href="/p/compcrimson/downloads/list" class="tab ">Downloads</a>
 
 
 
 
 
 <a href="/p/compcrimson/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/compcrimson/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/compcrimson/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 <form action="/p/compcrimson/source/browse" style="display: inline">
 
 Repository:
 <select name="repo" id="repo" style="font-size: 92%" onchange="submit()">
 <option value="default">default</option><option value="wiki">wiki</option>
 </select>
 </form>
 
 


 <span class="inst1"><a href="/p/compcrimson/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/compcrimson/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/compcrimson/source/list">Changes</a></span> &nbsp;
 <span class="inst4"><a href="/p/compcrimson/source/clones">Clones</a></span> &nbsp; 
 &nbsp;
 
 
 <form action="/p/compcrimson/source/search" method="get" style="display:inline"
 onsubmit="document.getElementById('codesearchq').value = document.getElementById('origq').value">
 <input type="hidden" name="q" id="codesearchq" value="">
 <input type="text" maxlength="2048" size="38" id="origq" name="origq" value="" title="Google Code Search" style="font-size:92%">&nbsp;<input type="submit" value="Search Trunk" name="btnG" style="font-size:92%">
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/compcrimson/source/browse/">git</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/compcrimson/source/browse/pytz/">pytz</a><span class="sp">/&nbsp;</span>tzfile.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/compcrimson/source/browse/pytz/tzfile.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper"><b>e87ef8b7cfd1</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_112"

><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_113"

><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_114"

><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_115"

><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_116"

><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_117"

><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_118"

><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_119"

><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_120"

><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_121"

><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_122"

><td id="122"><a href="#122">122</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_1

><td class="source">#!/usr/bin/env python<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_2

><td class="source">&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_3

><td class="source">$Id: tzfile.py,v 1.8 2004/06/03 00:15:24 zenzen Exp $<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_4

><td class="source">&#39;&#39;&#39;<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_5

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_6

><td class="source">from cStringIO import StringIO<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_7

><td class="source">from datetime import datetime, timedelta<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_8

><td class="source">from struct import unpack, calcsize<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_9

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_10

><td class="source">from pytz.tzinfo import StaticTzInfo, DstTzInfo, memorized_ttinfo<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_11

><td class="source">from pytz.tzinfo import memorized_datetime, memorized_timedelta<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_12

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_13

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_14

><td class="source">def build_tzinfo(zone, fp):<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_15

><td class="source">    head_fmt = &#39;&gt;4s c 15x 6l&#39;<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_16

><td class="source">    head_size = calcsize(head_fmt)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_17

><td class="source">    (magic, format, ttisgmtcnt, ttisstdcnt,leapcnt, timecnt,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_18

><td class="source">        typecnt, charcnt) =  unpack(head_fmt, fp.read(head_size))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_19

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_20

><td class="source">    # Make sure it is a tzfile(5) file<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_21

><td class="source">    assert magic == &#39;TZif&#39;<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_22

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_23

><td class="source">    # Read out the transition times, localtime indices and ttinfo structures.<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_24

><td class="source">    data_fmt = &#39;&gt;%(timecnt)dl %(timecnt)dB %(ttinfo)s %(charcnt)ds&#39; % dict(<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_25

><td class="source">        timecnt=timecnt, ttinfo=&#39;lBB&#39;*typecnt, charcnt=charcnt)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_26

><td class="source">    data_size = calcsize(data_fmt)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_27

><td class="source">    data = unpack(data_fmt, fp.read(data_size))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_28

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_29

><td class="source">    # make sure we unpacked the right number of values<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_30

><td class="source">    assert len(data) == 2 * timecnt + 3 * typecnt + 1<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_31

><td class="source">    transitions = [memorized_datetime(trans)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_32

><td class="source">                   for trans in data[:timecnt]]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_33

><td class="source">    lindexes = list(data[timecnt:2 * timecnt])<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_34

><td class="source">    ttinfo_raw = data[2 * timecnt:-1]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_35

><td class="source">    tznames_raw = data[-1]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_36

><td class="source">    del data<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_37

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_38

><td class="source">    # Process ttinfo into separate structs<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_39

><td class="source">    ttinfo = []<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_40

><td class="source">    tznames = {}<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_41

><td class="source">    i = 0<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_42

><td class="source">    while i &lt; len(ttinfo_raw):<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_43

><td class="source">        # have we looked up this timezone name yet?<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_44

><td class="source">        tzname_offset = ttinfo_raw[i+2]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_45

><td class="source">        if tzname_offset not in tznames:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_46

><td class="source">            nul = tznames_raw.find(&#39;\0&#39;, tzname_offset)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_47

><td class="source">            if nul &lt; 0:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_48

><td class="source">                nul = len(tznames_raw)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_49

><td class="source">            tznames[tzname_offset] = tznames_raw[tzname_offset:nul]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_50

><td class="source">        ttinfo.append((ttinfo_raw[i],<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_51

><td class="source">                       bool(ttinfo_raw[i+1]),<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_52

><td class="source">                       tznames[tzname_offset]))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_53

><td class="source">        i += 3<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_54

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_55

><td class="source">    # Now build the timezone object<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_56

><td class="source">    if len(transitions) == 0:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_57

><td class="source">        ttinfo[0][0], ttinfo[0][2]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_58

><td class="source">        cls = type(zone, (StaticTzInfo,), dict(<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_59

><td class="source">            zone=zone,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_60

><td class="source">            _utcoffset=memorized_timedelta(ttinfo[0][0]),<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_61

><td class="source">            _tzname=ttinfo[0][2]))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_62

><td class="source">    else:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_63

><td class="source">        # Early dates use the first standard time ttinfo<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_64

><td class="source">        i = 0<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_65

><td class="source">        while ttinfo[i][1]:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_66

><td class="source">            i += 1<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_67

><td class="source">        if ttinfo[i] == ttinfo[lindexes[0]]:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_68

><td class="source">            transitions[0] = datetime.min<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_69

><td class="source">        else:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_70

><td class="source">            transitions.insert(0, datetime.min)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_71

><td class="source">            lindexes.insert(0, i)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_72

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_73

><td class="source">        # calculate transition info<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_74

><td class="source">        transition_info = []<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_75

><td class="source">        for i in range(len(transitions)):<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_76

><td class="source">            inf = ttinfo[lindexes[i]]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_77

><td class="source">            utcoffset = inf[0]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_78

><td class="source">            if not inf[1]:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_79

><td class="source">                dst = 0<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_80

><td class="source">            else:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_81

><td class="source">                for j in range(i-1, -1, -1):<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_82

><td class="source">                    prev_inf = ttinfo[lindexes[j]]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_83

><td class="source">                    if not prev_inf[1]:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_84

><td class="source">                        break<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_85

><td class="source">                dst = inf[0] - prev_inf[0] # dst offset<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_86

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_87

><td class="source">                if dst &lt;= 0: # Bad dst? Look further.<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_88

><td class="source">                    for j in range(i+1, len(transitions)):<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_89

><td class="source">                        stdinf = ttinfo[lindexes[j]]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_90

><td class="source">                        if not stdinf[1]:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_91

><td class="source">                            dst = inf[0] - stdinf[0]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_92

><td class="source">                            if dst &gt; 0:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_93

><td class="source">                                break # Found a useful std time.<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_94

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_95

><td class="source">            tzname = inf[2]<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_96

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_97

><td class="source">            # Round utcoffset and dst to the nearest minute or the<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_98

><td class="source">            # datetime library will complain. Conversions to these timezones<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_99

><td class="source">            # might be up to plus or minus 30 seconds out, but it is<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_100

><td class="source">            # the best we can do.<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_101

><td class="source">            utcoffset = int((utcoffset + 30) / 60) * 60<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_102

><td class="source">            dst = int((dst + 30) / 60) * 60<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_103

><td class="source">            transition_info.append(memorized_ttinfo(utcoffset, dst, tzname))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_104

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_105

><td class="source">        cls = type(zone, (DstTzInfo,), dict(<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_106

><td class="source">            zone=zone,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_107

><td class="source">            _utc_transition_times=transitions,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_108

><td class="source">            _transition_info=transition_info))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_109

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_110

><td class="source">    return cls()<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_111

><td class="source"><br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_112

><td class="source">if __name__ == &#39;__main__&#39;:<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_113

><td class="source">    import os.path<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_114

><td class="source">    from pprint import pprint<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_115

><td class="source">    base = os.path.join(os.path.dirname(__file__), &#39;zoneinfo&#39;)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_116

><td class="source">    tz = build_tzinfo(&#39;Australia/Melbourne&#39;,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_117

><td class="source">                      open(os.path.join(base,&#39;Australia&#39;,&#39;Melbourne&#39;), &#39;rb&#39;))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_118

><td class="source">    tz = build_tzinfo(&#39;US/Eastern&#39;,<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_119

><td class="source">                      open(os.path.join(base,&#39;US&#39;,&#39;Eastern&#39;), &#39;rb&#39;))<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_120

><td class="source">    pprint(tz._utc_transition_times)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_121

><td class="source">    #print tz.asPython(4)<br></td></tr
><tr
id=sl_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_122

><td class="source">    #print tz.transitions_mapping<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/compcrimson/source/detail?spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac&amp;r=550fef0d0b3cc8780a645e6c68e7c5447d51b868">550fef0d0b3c</a>
 by Kevin Jerry Zhang &lt;kzh...@college.harvard.edu&gt;
 on Feb 22, 2012
 &nbsp; <a href="/p/compcrimson/source/diff?spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac&r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;format=side&amp;path=/pytz/tzfile.py&amp;old_path=/pytz/tzfile.py&amp;old=">Diff</a>
 </div>
 <pre>Corrected dates to EST with DST checks
</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/compcrimson/source/detail?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac';
 var publish_url = '/p/compcrimson/source/detail?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/ads.html');
 changed_urls.push('/p/compcrimson/source/browse/ads.html?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/app.yaml');
 changed_urls.push('/p/compcrimson/source/browse/app.yaml?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/hours.html');
 changed_urls.push('/p/compcrimson/source/browse/hours.html?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/images/dropped-d.png');
 changed_urls.push('/p/compcrimson/source/browse/images/dropped-d.png?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/images/dropped-s.png');
 changed_urls.push('/p/compcrimson/source/browse/images/dropped-s.png?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/info.html');
 changed_urls.push('/p/compcrimson/source/browse/info.html?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/main.py');
 changed_urls.push('/p/compcrimson/source/browse/main.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/__init__.py');
 changed_urls.push('/p/compcrimson/source/browse/pytz/__init__.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/__init__.pyc');
 changed_urls.push('/p/compcrimson/source/browse/pytz/__init__.pyc?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/gae.py');
 changed_urls.push('/p/compcrimson/source/browse/pytz/gae.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/reference.py');
 changed_urls.push('/p/compcrimson/source/browse/pytz/reference.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/tzfile.py');
 changed_urls.push('/p/compcrimson/source/browse/pytz/tzfile.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 var selected_path = '/pytz/tzfile.py';
 
 
 changed_paths.push('/pytz/tzfile.pyc');
 changed_urls.push('/p/compcrimson/source/browse/pytz/tzfile.pyc?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/tzinfo.py');
 changed_urls.push('/p/compcrimson/source/browse/pytz/tzinfo.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/tzinfo.pyc');
 changed_urls.push('/p/compcrimson/source/browse/pytz/tzinfo.pyc?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/pytz/zoneinfo.zip');
 changed_urls.push('/p/compcrimson/source/browse/pytz/zoneinfo.zip?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/util.py');
 changed_urls.push('/p/compcrimson/source/browse/util.py?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 changed_paths.push('/util.pyc');
 changed_urls.push('/p/compcrimson/source/browse/util.pyc?r\x3d550fef0d0b3cc8780a645e6c68e7c5447d51b868\x26spec\x3dsvne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/compcrimson/source/browse/ads.html?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/ads.html</option>
 
 <option value="/p/compcrimson/source/browse/app.yaml?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/app.yaml</option>
 
 <option value="/p/compcrimson/source/browse/hours.html?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/hours.html</option>
 
 <option value="/p/compcrimson/source/browse/images/dropped-d.png?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/images/dropped-d.png</option>
 
 <option value="/p/compcrimson/source/browse/images/dropped-s.png?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/images/dropped-s.png</option>
 
 <option value="/p/compcrimson/source/browse/info.html?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/info.html</option>
 
 <option value="/p/compcrimson/source/browse/main.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/main.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/__init__.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/__init__.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/__init__.pyc?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/__init__.pyc</option>
 
 <option value="/p/compcrimson/source/browse/pytz/gae.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/gae.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/reference.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/reference.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/tzfile.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 selected="selected"
 >/pytz/tzfile.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/tzfile.pyc?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/tzfile.pyc</option>
 
 <option value="/p/compcrimson/source/browse/pytz/tzinfo.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/tzinfo.py</option>
 
 <option value="/p/compcrimson/source/browse/pytz/tzinfo.pyc?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/tzinfo.pyc</option>
 
 <option value="/p/compcrimson/source/browse/pytz/zoneinfo.zip?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/pytz/zoneinfo.zip</option>
 
 <option value="/p/compcrimson/source/browse/util.py?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/util.py</option>
 
 <option value="/p/compcrimson/source/browse/util.pyc?r=550fef0d0b3cc8780a645e6c68e7c5447d51b868&amp;spec=svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac"
 
 >/util.pyc</option>
 
 </select>
 </td></tr></table>
 
 
 



 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 <a href="/p/compcrimson/source/list?path=/pytz/tzfile.py&r=550fef0d0b3cc8780a645e6c68e7c5447d51b868">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 4340 bytes,
 122 lines</div>
 
 <div><a href="//compcrimson.googlecode.com/git/pytz/tzfile.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac': '/pytz/tzfile.py'}
 codereviews = CR_controller.setup(
 {"projectName":"compcrimson","loggedInUserEmail":"whhhmarks@gmail.com","profileUrl":"/u/100545230244848929459/","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13882333484250518008","token":"QAxhIW9WGzKiMfpWCuaOQHxnc6o:1354171146555","projectHomeUrl":"/p/compcrimson","relativeBaseUrl":"","assetHostPath":"https://ssl.gstatic.com/codesite/ph","domainName":null}, '', 'svne87ef8b7cfd1fcfcf7a7ad8308624232cd1efdac', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13882333484250518008/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

