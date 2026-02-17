## A4.4 Emulated Data Aborts

ISVYDC

On REC exit due to Emulatable Data Abort, sufficient information is provided to the Host to enable it to emulate the access, for example to emulate a virtual peripheral.

On taking the REC exit, the Host can either

- Establish a mapping in the RTT, in which case it would want the Realm to re-attempt the access. In this case, on the next REC entry the Host sets enter.flags.emul\_mmio = RMI\_NOT\_EMULATED\_MMIO , which indicates that instruction emulation was not performed. This causes the return address to be the faulting instruction.
- Emulate the access. For an emulated write, the data is provided in exit.gprs[0] . For an emulated read, the data is provided in enter.gprs[0] . In this case, on the next REC entry the Host sets enter.flags.emul\_mmio = RMI\_EMULATED\_MMIO , which indicates that the instruction was emulated. This causes the return address to be the address of the instruction which generated the Data Abort plus 4 bytes.

## See also:

- A4.2.3 REC entry following REC exit due to Data Abort
- A4.3.4.3 REC exit due to Data Abort
- A5.2.1 Realm IPA space

## A4.5 Host call

This section describes the programming model for Realm communication with the Host.

- DYDJWT A Host call is a call made by the Realm to the Host, by execution of the RSI\_HOST\_CALL command.
- IXNFKZ A Host call can be used by a Realm to make a hypercall.
- RDNBQF On Realm execution of HVC, an Unknown exception is taken to the Realm.

See also:

- A4.2.2 General purpose registers restored on REC entry
- A4.3.9 REC exit due to Host call
- B5.3.4 RSI\_HOST\_CALL command
- D1.3.2 Host call flow