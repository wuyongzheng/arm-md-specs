## A10.6 Planes debug and performance monitoring

This section describes the debug and performance monitoring features which are available to Pn.

## A10.6.1 Planes PMU

- On Plane exit, plane\_exit.pmu\_ovf\_status indicates the status of the PMU overflow at the time of the Plane exit.
- The number of PMU counters available to Pn is determined by the value of RmiRealmParams::pmu\_num\_ctrs. See also:
- A3.6 Realm support for Performance Monitors Extension
- A10.2.3 Plane exit

## A10.6.2 Planes debug

- The number of breakpoints available to Pn is determined by the value of RmiRealmParams::num\_bps.
- The number of watchpoints available to Pn is determined by the value of RmiRealmParams::num\_wps.
- On a debug exception which is taken from Pn, if plane\_enter.flags.trap\_dbg == RSI\_TRAP then a Plane exit due to Synchronous Exception occurs.
- Setting plane\_enter.flags.trap\_dbg == RSI\_TRAP causes the RMM to set MDCR\_EL2.TDE = '1' during Plane entry.

See also:

- [A3.5 Realm support for self-hosted debug](rmm-A3.md#a35-realm-support-for-self-hosted-debug)

