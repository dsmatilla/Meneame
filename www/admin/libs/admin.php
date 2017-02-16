<?php


$globals['extra_js'][] = 'autocomplete/jquery.autocomplete.min.js';
$globals['extra_js'][] = 'jquery.user_autocomplete.js';
$globals['extra_css'][] = 'jquery.autocomplete.css';
$globals['extra_css'][] = 'bootstrap.min.css';
$globals['extra_css'][] = 'bootstrap-theme.min.css';
$globals['extra_css'][] = 'admin.css';
$globals['extra_js'][] = '../admin/js/admin.js';
$globals['ads'] = false;

if (!$current_user->admin) {
	Haanga::Load("admin/no_access.html");
	do_footer();
	die;
}

function do_admin_tabs($tab_selected = false)
{
	$tabs = [
		"hostname" => 'bans.php?tab=hostname',
		"punished_hostname" => 'bans.php?tab=punished_hostname',
		"email" => 'bans.php?tab=email',
		"ip" => 'bans.php?tab=ip',
		"words" => 'bans.php?tab=words',
		"proxy" => 'bans.php?tab=proxy',
		"noaccess" => 'bans.php?tab=noaccess',
		"admin_logs" => 'logs.php',
		"comment_reports" => 'reports.php',
		"strikes" => 'strikes.php'
	];

	Haanga::Load("admin/tabs.html", compact('tabs', 'tab_selected'));
}