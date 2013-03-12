/* Load this script using conditional IE comments if you need to support IE 7 and IE 6. */

window.onload = function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'icomoon\'">' + entity + '</span>' + html;
	}
	var icons = {
			'icon-cc' : '&#xe000;',
			'icon-twitter' : '&#xe001;',
			'icon-google-plus' : '&#xe002;',
			'icon-linkedin' : '&#xe003;',
			'icon-github' : '&#xe004;',
			'icon-feed' : '&#xe005;',
			'icon-mail' : '&#xe006;',
			'icon-bubble' : '&#xe00a;',
			'icon-info' : '&#xe007;'
		},
		els = document.getElementsByTagName('*'),
		i, attr, html, c, el;
	for (i = 0; i < els.length; i += 1) {
		el = els[i];
		attr = el.getAttribute('data-icon');
		if (attr) {
			addIcon(el, attr);
		}
		c = el.className;
		c = c.match(/icon-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
};