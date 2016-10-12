
agent_name=fence_powerman
sbindir=/usr/sbin
mandir=/usr/share/man/man8

check:
	echo No tests implemented

install:
	install -D -m 0755 $(agent_name) $(DESTDIR)$(sbindir)/$(agent_name) 
	install -D -m 0644 $(agent_name).8 $(DESTDIR)$(mandir)/$(agent_name).8
