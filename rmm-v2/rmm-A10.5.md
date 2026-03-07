## A10.5 Planes timers

- On REC exit from P0, the Realm EL1 timer state reported to the Host is P0's EL1 timer state.
- A Realm EL1 timer is active if it is enabled and unmasked.
- On REC exit from Pn, for each of the EL1 virtual and physical timers, if any of the following is true then the timer state reported to the Host is Pn's EL1 timer state:
- The Pn timer is active and the P0 timer is not active.
- Both Pn and P0 timers are active and the Pn timer deadline is earlier than the P0 timer deadline.

Otherwise, the timer state reported to the Host is P0's EL1 timer state.

- The following table summarises the timer state which is reported to the Host on REC exit.

|   P0 active |   Pn active | Earliest CVAL   | Reported to Host   |
|-------------|-------------|-----------------|--------------------|
|           0 |           0 | P0              | P0                 |
|           0 |           0 | Pn              | P0                 |
|           0 |           1 | P0              | Pn                 |
|           0 |           1 | Pn              | Pn                 |
|           1 |           0 | P0              | P0                 |
|           1 |           0 | Pn              | P0                 |
|           1 |           1 | P0              | P0                 |
|           1 |           1 | Pn              | Pn                 |

On Plane exit, Pn's EL1 timer state is exposed to P0 via the RsiPlaneExit object.

P0 software should check the Realm EL1 timer state on every return from RSI\_PLANE\_ENTER and update virtual interrupt state accordingly. This is true regardless of the value of exit.exit\_reason : even if the return occurred for a reason unrelated to timers (for example, a Plane exit due to Data Abort), the Realm EL1 timer state should be checked.


On Plane entry, the RMM may mask the hardware timer signal, following the same logic as for REC entry.

Management of EL1 timer state for a Realm with multiple Planes can be implemented by multiplexing the following into the EL2 hardware timers:

- P0's EL1 timers
- The Host's EL2 timers

## See also:

- [A6.2 Realm timers](rmm-A6.2.md)
- [A10.2.3 Plane exit](rmm-A10.2.md#a1023-plane-exit)
- [B5.5.15 RsiPlaneExit type](rmm-B5.5.md#b5515-rsiplaneexit-type)