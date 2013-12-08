pcap
====

Flag: **use_ssl_dude**

![pcap](images/pcap.png "pcap challenge introduction")

The challenge flavortext says "Check out this [pcap](pcap.pcap "pcap")".

Opening the packet capture file with Wireshark, we see one HTTP (and thus
unencrypted) POST containing login credentials:

![pcap](images/pcap_post1.png "pcap challenge introduction")

And then a second, which contains our flag:

![pcap](images/pcap_post2.png "pcap challenge introduction")

The flag is thus `use_ssl_dude`.

[« Return to challenge board](../README.md "Return to challenge board")
