---
title: ZODB analysis
date: 2013-02-22 23:40
tags: [development, plone]
---

A note to myself on how to get a quick insight in the content in a
ZODB.

A couple of years ago I created
[mr.inquisition](http://pypi.python.org/pypi/mr.inquisition/) to get
more insight in the content of a foreign Zope Object Database
(ZODB). And while I still believe it still may have its uses (although
I haven't personally used it for a while), you may want to start off
with the following command:

    $ bin/zopepy -m ZODB.scripts.analyze var/filestorage/Data.fs

This results in for example:

    Processed 10611 records in 150 transactions
    Average record size is  571.80 bytes
    Average transaction size is 40449.41 bytes
    Types used:
    Class Name                                  Count   TBytes    Pct AvgSize
    ------------------------------------------ ------ --------  ----- -------
    AccessControl.users.User                        2      262   0.0%  131.00
    App.ApplicationManager.ApplicationManager       1      107   0.0%  107.00
    App.Product.ProductFolder                       1       34   0.0%   34.00
    BTrees.IIBTree.IIBTree                        302    64876   1.1%  214.82
    BTrees.IIBTree.IITreeSet                     1952   114421   1.9%   58.62
    ...
    webdav.LockItem.LockItem                       22     5817   0.1%  264.41
    ...PersistentAdapterRegistry                    3    13840   0.2% 4613.33
    zope.ramcache.ram.RAMCache                      1      288   0.0%  288.00
    ========================================== ====== ========  ===== =======
                            Total Transactions    150                  39.50k
                                 Total Records  10611    5925k 100.0%  571.80
                               Current Objects   6286    2696k  45.5%  439.25
                                   Old Objects   4325    3228k  54.5%  764.46


Thanks to an article by Nejc Zupan from about a week ago
([Dexterity vs. Archetypes](http://www.niteoweb.com/blog/dexterity-vs.-archetypes))
in which he used this---at least for me---hidden gem.
