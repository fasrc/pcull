#
# This script should write the message used for the body of emails sent by 
# pcull when it kills processes.  Note that this is sourced from the main 
# script, so any variables defined there are available for use here.
#

cat <<EOF
Hello Odyssey Cluster User,

This is an automated message from Odyssey access node $HOSTNAME.  One of the processes you were running exceeded the memory limit that we've put in place to keep the access nodes responsive for all users.  Thus, your process has been killed.

Processes that use too much CPU are lowered in priority; processes that use too much memory or run with too much CPU for too long are killed.  (Typical programs that are meant for interactive use, such as common editors, compilers, and filesystem utilities, are exempt from these limits.)

Please be aware that CPU and/or memory intensive jobs must be executed via the LSF batch job system, and not directly on the Odyssey access nodes.  You can submit your job to one of the non-interactive LSF queues, or you can run it interactively in LSF by executing a command like:

  bsub -Is -q interact $shortcmd

Please see our FAQ at http://rc.fas.harvard.edu/ or contact rchelp@fas.harvard.edu for more information about using Odyssey.


Process details:

USER : $user
PID  : $pid
CMD  : $fullcmd
%CPU : $pcpu  (limit: $RENICE_IF_PCPU_GT)
%MEM : $pmem  (limit: $KILL_IF_PMEM_GT)
ETIME: $etime (limit: $KILL_IF_PCPU_GT_AND_LIFETIME_GT)
EOF
