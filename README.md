# pcull
kill or renice processes that are overusing resources

See `pcull --help` for more information.  The output of that is reproduced
here, but may be out of date:

```
-------------------------------------------------------------------------------


NAME
    pcull - kill or renice processes that are overusing resources

SYNOPSIS
    pcull [--daemonize --loop --log-file=/SOME/FILE] [--debug --pretend]

DESCRIPTION
    This scripts takes action on processes that exceed resource limits defined
    in its configuration file, /etc/pcull/pcull.conf by default.  Currently, it
    renices processes that use too much CPU for a relatively short time, kills
    processes that use too much CPU for a relatively long time, and kills
    processes that use too much memory.  The culling does not kick in unless
    load avg or free memory are above/below the thresholds specified in the
    configuration file.  CPU-intensive jobs are also given a short grace period
    before being reniced, again set in the configuration file.  When this
    script takes culling actions, e-mail is sent to the affected user and any
    other users specified in the configuration file.

    The files /etc/pcull/exempt_users and /etc/pcull/exempt_processes can be
    used to specify users and processes (as regular expressions) that are to be
    exempt from culling.  The root user is automatically exempt.  The files
    /etc/pcull/*_subject.sh and /etc/pcull/*_body.sh are scripts that build the
    subject and body of emails that are sent out.  See the comments in those
    files for more details.

    The base configuration directory, /etc/pcull by default, is actually
    computed relative to the location of the pcull script.

    The following call will run pcull once and simply print to stderr the
    actions it would take:

        pcull --pretend --debug

    The following call will run pcull forever in the background, renicing
    and killing jobs that exceed resource limits:

        pcull --daemonize --loop --log-file=/var/log/pcull

    The rpm package of this script provides an init script which can be used to
    control pcull running in looping, daemonized mode.  Any arguments passed to
    start are passed on to the pcull script.  By default, the init script will
    configure pcull to write its log to /var/log/pcull.log.

OPTIONS
    --pretend
        only write to the log, don't take any real action

    --debug
        write extra verbose information to the log

    --log-file
        path of where to write log messages; must be an absolute path; default
        is /dev/stderr

    --daemonize
        detach from the terminal, run in the background, etc.

    --loop
        execute forever in a loop; see configuration file option LOOP_INTERVAL

    -h, --help
        print this help and exit

KNOWN BUGS
    One SIGHUP will cause the script to properly reload the configuration, but
    further SIGHUPs appear to be ignored.

AUTHOR
    Copyright (c) 2009-2013
    Harvard FAS Research Computing
    John Brunelle <john_brunelle@harvard.edu>
```
