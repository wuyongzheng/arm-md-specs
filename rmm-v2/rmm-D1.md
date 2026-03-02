## Chapter D1 Flows

This section presents flows which explain how the RMM architecture can be used by the Host, and by Realm software.

Note that parts of the sequences below are for illustration only. For example, in the Realm creation flows, the RMI\_GRANULE\_RANGE\_DELEGATE and RMI\_GRANULE\_RANGE\_UNDELEGATE commands are called immediately before or after the RMI\_X\_CREATE and RMI\_X\_DESTROY commands respectively. An alternative flow would be for the Host to maintain a pool of Granules in the GRAN\_DELEGATED state, from which RMM data structures and Realm data can be allocated on demand.

DRAFT