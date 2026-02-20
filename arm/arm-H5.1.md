## H5.1 About the Embedded Cross-Trigger

The Embedded Cross-Trigger (ECT) allows a debugger to:

- Send trigger events to a PE. For example, this might be done to halt the PE.
- Send a trigger event to one or more PEs, or other system components, when a trigger event occurs on another PE or system component. For example, this might be done to halt all PEs when one individual PE halts.

Figure H5-1 shows the logical structure of an ECT.

Figure H5-1 Structure of an Embedded Cross-Trigger

<!-- image -->

The ECT can deliver many types of trigger events, which are described in the following sections:

- Debug request trigger event.
- Restart request trigger event.
- Cross-halt trigger event.
- Performance Monitors overflow trigger event.
- Generic trace external input trigger events.
- Generic trace external output trigger events.
- Generic CTI interrupt trigger event.

From the introduction of Armv8, an A-profile implementation must:

- Include a Cross-Trigger interface, CTI.
- Implement at least the input and output triggers defined in this architecture.

In addition, see Cross-triggers on a PE in an Arm A-profile implementation.

Arm recommends that this Cross-Trigger interface includes:

- The ability to route trigger events between Trace Units, which typically have advanced event triggering logic.
- An output trigger to the interrupt controller.

Also, Arm recommends that the Embedded Cross-Trigger includes the capability to send and receive IMPLEMENTATION DEFINED system trigger events to and from other system components, including a system counter, using a system CTI. See Halt-on-debug.

Note

The ECT and CTI must only signal trigger events for external debugging. They must not route software events, such as interrupts. For example, the Performance Monitors overflow input trigger is provided to allow entry to Debug state on a counter overflow, and the output trigger to the interrupt controller is provided to generally allow events from the external debug subsystem to be routed to a software agent. However, the combination of the two must not be used as a mechanism to route Performance Monitors overflows to an interrupt controller.

Note

CTI version 1 (CTIv1) is defined by the CoreSight™ SoC Technical Reference Manual . CTIv2 extends CTIv1 with the addition of the input channel gate. See Implementation with CTIv2.

## H5.1.1 Implementation with a CoreSight CTI

For details of the recommended connections for an A-profile implementation, see Recommended External Debug Interface. See also CoreSight™ SoC Technical Reference Manual.

## H5.1.2 Implementation with CTIv2

If the CTI implemented is CTIv2 then:

- The CTIDEVARCH, CTIDEVAFF0, and CTIDEVAFF1 registers must be implemented.
- If the channel gate function is implemented, it applies to both input and output channels.
- The input channel gate function must be implemented if either of the following is true:
- -The CTM is implemented and the architecture variant is Armv8.5 or higher.
- -The CTIDEVARCH.REVISION field reads as 0b0001 or higher.

Implementation of CTIv2 features in architecture variants below Armv8.5 is OPTIONAL, but Arm recommends that CTIv2 is implemented, CTIv2 must be implemented from Armv8.5.