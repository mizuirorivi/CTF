# Ez

## What we noticed

* this service use caddy
* caddy is web server
* may use FastCGI protocol because the caddy execute php
* caddy 2.4.5

## suspicious git issue

* https://github.com/caddyserver/caddy/issues/5278
* https://github.com/caddyserver/caddy/issues/4466
* https://github.com/caddyserver/caddy/issues/3410
* https://github.com/caddyserver/caddy/issues/3100

## result that seeing writeups


this is Caddy File.

```
{
    admin off
    local_certs  # Let's not spam Let's Encrypt
}

caddy.chal-kalmarc.tf {
    redir https://www.caddy.chal-kalmarc.tf
}

#php.caddy.chal-kalmarc.tf {
#    php_fastcgi localhost:9000
#}

flag.caddy.chal-kalmarc.tf {
    respond 418
}

*.caddy.chal-kalmarc.tf {
    encode zstd gzip
    log {
        output stderr
        level DEBUG
    }

    # block accidental exposure of flags:
    respond /flag.txt 403

    tls /etc/ssl/certs/caddy.pem /etc/ssl/private/caddy.key {
        on_demand
    }

    file_server {
        root /srv/{host}/
    }
}
```

```root /srv/{host}/``` meant that  when request came to service, since hostname replace {host}, can allow access to /srv/hostname .

this come from the ["placeholder"](https://caddyserver.com/docs/conventions#placeholders) of caddy

Now let's see the challenge,

since php is disabled.

this means that traversing to the https://php.caddy.chal-kalmarc.tf/index.php will not call the php iinterpreter to evaluate the code.



according to writeup, it seem to following two cve's connected closely this challenge

* https://github.com/advisories/GHSA-2927-hv3p-f3vp
* https://github.com/advisories/GHSA-qpm3-vr34-h8w8

According to  chat from kalmar ctf of channel on discord,

vuln can exist by [CVE-2022-29718](https://github.com/advisories/GHSA-2927-hv3p-f3vp) 

there were [good forum](https://caddy.community/t/php-fastcgi-phishing-redirection/14542/15)

![](/home/r3v321se/Projects/ctf/2023/KalmarCTF/web/Ez/forum.png)

so i tried

```
GET /b/../flag.txt HTTP/2
Host: backups/php.caddy.chal-kalmarc.tf
```

i got flag!!

