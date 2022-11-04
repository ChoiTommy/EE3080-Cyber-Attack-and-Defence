<?php
$ip = $_SERVER['REMOTE_ADDR'];
$dt = date("l dS \of F Y h:i:s A");
$file=fopen("ip_log.txt","a");
$data = $ip.' '.$dt."\n";
fwrite($file, $data);
fclose($file);
header( 'Location: https://www.techrepublic.com/article/iphone-14-cheat-sheet/#:~:text=The%20iPhone%2014%20and%20iPhone%2014%20Plus%20feature%20an%20A15,image%20signal%20processor%20that%20works' ) ;
?>