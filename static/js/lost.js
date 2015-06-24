/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	JavaScript Document for GSS 404 lost page project
	Author: Brlog
	Year: 2014

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/
var html_id_original;

function takeOver404(){
	var html_el = document.getElementsByTagName("html")[0];
	html_id_original = html_el.id;
	html_el.id = 'lost_page_404_gss';
	var lost_css = '<style type="text/css">' +
			'html#lost_page_404_gss, #lost_page_404_gss body{ height:100%; width:100%; font-size:100%;}' +
			'#lost_page_404_gss body{ max-height:100%; overflow:hidden; margin:0; padding: 0; font-size:100%; }' +
			'#lost_page_404_gss p, #lost_page_404_gss a{ font-family: Arial, sans-serif; color:#ffffff; }' +
			'#lost_page_404_gss #lost_wrapper{ height:100%; width:100%; position: fixed; top:0; left:0; z-index:2147483647; background: #505050 url(http://www.gss.hr/gss_404/images/izgubljena-stranica-bkg.jpg); background-size: cover; text-align: center; font-family: Arial, sans-serif; color:#ffffff; }' +
			'#lost_page_404_gss .lost_content{ position: absolute; top:50%; left:50%; margin:-100px 0 0 -300px; width:600px; }' +
			'#lost_page_404_gss .lost_content h1{ margin:0; padding:0; text-indent: -9999px;  background: url(http://www.gss.hr/gss_404/images/txt-lost-page.png) no-repeat; width:218px; height: 25px; display: inline-block; font-size: 1.5em; line-height: 1.4em; }' +
			'#lost_page_404_gss .lost_content p{ font-size: 0.875em; padding:0; margin:10px 0; }' +
			'#lost_page_404_gss .lost_content .gss_logo{ padding:0; margin:15px 0; display: inline-block; }' +
			'#lost_page_404_gss .lost_content .gss_logo img{ height:100px; }' +
			'#lost_page_404_gss a.lost_close{ font-size: 0.875em; color:#ffffff; text-decoration: underline; background:none; border:none; display: inline-block; text-align: center; width:200px; bottom: 90px; left:50%; margin-left: -100px; position: absolute; }' +
			'#lost_page_404_gss a.lost_close:hover{ text-decoration: none; color:#ffffff; background:none; border:none; }' +
			'#lost_page_404_gss .lost_content p, #lost_page_404_gss .lost_close{ font-weight: normal; }' +
			'#lost_page_404_gss #lost_wrapper .copy{ font-size: 0.688em; width:200px; position: absolute; bottom: 10px; left:50%; margin-left: -100px; }' +
			'@media all and (-webkit-min-device-pixel-ratio: 2), all and (min--moz-device-pixel-ratio: 2) { #lost_page_404_gss .lost_content h1{ background-image:url(http://www.gss.hr/gss_404/images/txt-lost-page@2x.png); background-size:218px 25px; }}' +
			'@media only screen and (max-width: 37.5em) { #lost_page_404_gss .lost_content{ width:90%; top:20%; left:5%; margin:0; }}' +
			'@media only screen and (max-width: 22.5em) { #lost_page_404_gss .lost_content h1{ background-size:90%; }}' +
		'</style>';

	var lost_html = document.createElement('div');
	lost_html.id = 'lost_wrapper';
	lost_html.innerHTML = '<div class="lost_content"><h1>This page got lost!</h1><p>If the same should ever happen to you, just be sure you can count on us.</p><a class="gss_logo" href="http://www.gss.hr"><img src="http://www.gss.hr/gss_404/images/gss-logo.svg" height="100" alt="HGSS"></a></div><a href="javascript:history.back()" class="lost_close" id="lost_close">back</a>';

	var lost_body = document.body;

	lost_body.innerHTML = lost_css + lost_body.innerHTML;
	lost_body.appendChild(lost_html);

}

function close404(){
	var lost_el = document.getElementById('lost_wrapper');
	lost_el.parentNode.removeChild(lost_el);
	var html_el = document.getElementsByTagName("html")[0];
	html_el.id = html_id_original;
}

window.onload=function(){

	takeOver404();

	var close_el = document.getElementById('lost_close');
	close_el.onclick = function(e){
    	close404();
	}
};
