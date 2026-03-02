## Chapter A8 Realm debug and performance monitoring

This section describes the debug and performance monitoring features which are available to a Realm.

## A8.1 Realm PMU

This section describes the programming model for usage of PMU by a Realm.

- On REC entry, Realm PMU state is restored from the REC object.
- On REC exit, all Realm PMU state is saved to the REC object.
- On REC exit, exit.pmu\_ovf\_status indicates the status of the PMU overflow at the time of the Realm exit. See also:
- A3.1.5 Realm support for Performance Monitors Extension
- A4.3 REC exit
- B4.4.16 RmiRecExit type