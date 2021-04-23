# fence-agents-powerman

fence-agents-powerman provides a fence agent for use with pacemaker,
which uses powerman to control and monitor the power status of
hosts.

This fence agent requires powerman, pacemaker, and the fence-agents-common
packages to function.

This is just a packaged version of the powerman fence agent, for use while we wait
for Redhat to pull it into RHEL 8.  The bugzilla ticket for that is
https://bugzilla.redhat.com/show_bug.cgi?id=1952967

The tree for the fence agents is at:
https://github.com/ClusterLabs/fence-agents/tree/master/agents/

For an introduction to fencing, see http://clusterlabs.org/doc/crm_fencing.html
For other fence agents, see http://sourceware.org/cluster/wiki/
For pacemaker details, see https://github.com/ClusterLabs/pacemaker
For powerman details, see https://github.com/chaos/powerman
