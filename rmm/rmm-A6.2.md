## A6.2 Realm timers

This section describes the operation of architectural timers during Realm execution, including the following:

- The behavior of EL2 timers programmed by the Host
- The behavior of EL1 timers as perceived by the Realm
- The Realm timer state which is exposed to the Host on REC exit, in order to facilitate virtualization of timer interrupts
- RLKNDV Architectural timers are available to a Realm and behave according to their architectural specification.
- IVFYJV If the Host has programmed an EL1 timer to assert its output during Realm execution, that timer output is not guaranteed to assert.
- RFKCHX If the Host has programmed an EL2 timer to assert its output during Realm execution, that timer output is guaranteed to assert.
- RRJZRP Both the virtual and physical counter values are guaranteed to be monotonically increasing when read by a Realm, in accordance with the architectural counter behavior.
- RJSMQP A read by a Realm of either the virtual or physical counter at the same place in the instruction flow would return the same value.
- XYCDMW In order to ensure that the Realm has a consistent view of time, the virtual timer offset must be fixed for the lifetime of the Realm. The absolute value of the virtual timer offset is not important, so the value zero has been chosen for simplicity of both the specification and the implementation.
- IFKMGZ The rule that virtual and physical counter values are identical may need to be amended if a future version of the specification supports migration and / or virtualization of time based on the virtual counter differing from the physical counter.
- RSVCMR On a change in the output of an EL1 timer which requires a Realm-observable change to the state of virtual interrupts, a REC exit occurs.
- RVWQDH On REC exit, Realm EL1 timer state is exposed via the RmiRecExit object:
- exit.cntv\_ctl contains the value of CNTV\_CTL\_EL0 at the time of the Realm exit.
- exit.cntv\_cval contains the value of CNTV\_CVAL\_EL0 at the time of the Realm exit, expressed as if the virtual counter offset was zero.
- exit.cntp\_ctl contains the value of CNTP\_CTL\_EL0 at the time of the Realm exit.
- exit.cntp\_cval contains the value of CNTP\_CVAL\_EL0 at the time of the Realm exit, expressed as if the physical counter offset was zero.
- SPYWWF The Host should check the Realm EL1 timer state on every return from RMI\_REC\_ENTER and update virtual interrupt state accordingly. This is true regardless of the value of exit.exit\_reason : even if the return occurred for a reason unrelated to timers (for example, a REC exit due to Data Abort), the Realm EL1 timer state should be checked.
- IVRWGS On REC entry, for both the EL1 Virtual Timer and the EL1 Physical Timer, if the EL1 timer asserts its output in the state described in the REC exit structure from the previous REC exit then the RMM masks the hardware timer signal before returning to the Realm.

This masking is done to allow the Realm to make forward progress, which would otherwise be prevented by the hardware timer generating a physical interrupt that would cause a Realm exit.

During Realm execution, when the hardware timer signal is masked, the Realm may write to the timer registers, causing the hardware timer to become de-asserted and possibly asserted again. Such changes in the output of the EL1 timer are not required to result in a REC exit if the RMM can infer that the change should not result in a Realm-observable change to the state of virtual interrupts.

It is only when a change in the hardware timer output means that the corresponding virtual interrupt needs to be made pending or idle, that a REC exit must occur.

Chapter A6. Realm interrupts and timers A6.2. Realm timers

See also:

- A4.3 REC exit
- B4.4.16 RmiRecExit type
- D1.6.2 Timer interrupt delivery flow