# Set parameters in conf/config.xml #

## Include or Exclude Modules ##

```
    <modules name="auth" />
    <modules name="headers" />
    <modules name="cache" />
    <modules name="json" />
    <modules name="flash" />
    <modules name="xml" />
    <modules name="js" />
    <modules name="dom" />
    <modules name="csrf" />
    <modules name="session" />
    <modules name="fingerprint" />
    <modules name="main" />
```


## Set Path extLib ##
```
    <path flasm="../../core/extlib/flasm16mac" />
    <path js-beautify="../../core/extlib/js-beautify/index.html" />
    <path syntaxhighlighter="../../core/extlib/syntaxhighlighter_3.0.83" />
```

## Set Proxy ##

```

    <proxy proxy="False" />
    <proxy auth="False" />
    <proxy address="127.0.0.1:8080" />
    <proxy usr="admin" />
    <proxy psw="123" />

```

## Set Flasm to OS ##

```
    Mac
    <path flasm="../../core/extlib/flasm16mac" />

    Linux
    <path flasm="../../core/extlib/flasm16linux" />

    Windows
    <path flasm="../../core/extlib/flasm16win" />
```