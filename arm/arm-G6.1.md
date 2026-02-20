## G6.1 About the Generic Timer in AArch32 state

Figure G6-1 shows an example system-on-chip that uses the Generic Timer as a system timer. In this figure:

- This manual defines the architecture of the individual PEs in the multiprocessor blocks.
- The ARMGeneric Interrupt Controller Architecture Specification defines a possible architecture for the interrupt controllers.
- Generic Timer functionality is distributed across multiple components.

Figure G6-1 Generic Timer example

<!-- image -->

## The Generic Timer:

- Provides a system counter, that measures the passing of time in real-time.

Note

The Generic Timer can also provide other components at a system level, but Figure G6-1 does not show any such components.

- Supports virtual counters that measure the passing of virtual-time. That is, a virtual counter can measure the passing of time on a particular virtual machine.
- Timers, that can trigger events after a period of time has passed. The timers:
- -Can be used as count-up or as count-down timers.
- -Can operate in real-time or in virtual-time.

This chapter describes an instance of the Generic Timer component that Figure G6-1 shows as Timer\_0 or Timer\_1 within the Multiprocessor A or Multiprocessor B block. This component can be accessed from AArch64 state or AArch32 state, and this chapter describes access from AArch32 state. The Generic Timer in AArch64 state describes access to this component from AArch64 state.

Note

The reset requirements of Generic Timer registers are more strict when they are accessed from AArch32 state than when they are accessed from AArch64 state.

AGeneric Timer implementation must also include a memory-mapped system component. This component:

- Must provide the System counter shown in Figure G6-1.
- Optionally, can provide timer components for use at a system level.

System Level Implementation of the Generic Timer describes this memory-mapped component.

## G6.1.1 The full set of Generic Timer components

Within a system that might include multiple PEs, a full set of Generic Timer components is as follows:

## The system counter

This provides a uniform view of system time, see The system counter. Because this must be implemented at the system level, it is accessed through The system level memory-mapped implementation of the Generic Timer. However, during initialization, a status register in each implemented timer in the system must be programmed with the frequency of the system counter, so that software can read this frequency.

## PE implementations of the Generic Timer

Each PE implementation of the Generic Timer provides the following components:

- Aphysical counter, that gives access to the count value of the system counter. When FEAT\_ECV is implemented, EL2 is using AArch64, and EL2 is implemented and enabled in the current Security state, the CNTPOFF\_EL2 register allows offsetting of AArch32 physical timers and counters.
- Avirtual counter, that gives access to virtual time. In AArch32 state, the CNTVOFF register defines the offset between physical time, as defined by the value of the system counter, and virtual time.
- Anumber of timers. In an implementation where all Exception levels are implemented and can use AArch32 state, the timers that are accessible from AArch32 state are:
- -ASecure PL1 physical timer.
- -ANon-secure EL1 physical timer.
- -ANon-secure EL2 physical timer.
- -An EL1 virtual timer.
- -ANon-secure EL2 virtual timer.
- -ASecure EL2 virtual timer.
- -ASecure EL2 physical timer.

The Non-secure EL2 virtual timer is available when FEAT\_VHE is implemented. The Secure EL2 timers are available when FEAT\_SEL2 is implemented, but are only accessible in AArch32 state if using EL0, when EL0 is using AArch32, Secure EL2 is using AArch64, and the Effective value of HCR\_EL2.{E2H,TGE} is {1, 1}.

Note

The Secure PL1 physical timer uses the Secure banked instances of the CNTP\_CTL, CNTP\_CVAL, and CNTP\_TVAL registers, and the Non-secure EL1 physical timer uses the Non-secure instances of the same registers.

The AArch32 view of the Generic Timer describes these components.

## The system level memory-mapped implementation of the Generic Timer

The memory-mapped registers that control the components of the system level implementation of the Generic Timer are grouped into frames . The Generic Timer architecture defines the offset of each

## G6.1.2 The system counter

The Generic Timer provides a system counter with the following specification:

## Width

## Roll-over

register within its frame, but the base address of each frame is IMPLEMENTATION DEFINED, and defined by the system.

Each system level component has one or two register frames. The possible system level components are:

## The memory-mapped counter module, required

This module controls the system counter. It has two frames:

- Acontrol frame, CNTControlBase.
- Astatus frame, CNTReadBase.

## The memory-mapped timer control module, required

The system level implementation of the Generic Timer can provide up to eight timers, and the memory-mapped timer control module identifies:

- Which timers are implemented.
- The features of each implemented timer.

This module has a single frame, CNTCTLBase.

## Memory-mapped timers, optional

An implemented memory-mapped timer:

- Must provide a privileged view of the timer, in the CNTBase N frame.
- Optionally. provides an unprivileged view of the timer in the CNTEL0Base N frame.

N is the timer number, and the corresponding frame number, in the range 0 - 7.

System Level Implementation of the Generic Timer describes these components.

From Armv8.0 to Armv8.5 inclusive, at least 56 bits wide. The value returned by any 64-bit read of the counter is zero-extended to 64 bits.

From Armv8.6, must be 64 bits wide.

## Effective frequency

This indicates the amount of time each unit of the counter represents. For example:

- An effective frequency of 50MHz means each unit of the counter represents 20ns.
- An effective frequency of 1GHz means each unit of the counter represents 1ns.
- The effective frequency is indicated in the CNTFRQ register.

From Armv8.0 to Armv8.5 inclusive, the effective frequency is a fixed value, typically in the range 1-50MHz.

From Armv8.6, the effective frequency is a fixed value of 1GHz.

The counter might not be driven by a clock running at the effective frequency. For example, a counter with an effective frequency of 1GHz might have an actual clock running at 125MHz but the counter increments by 8 on each tick of the clock.

Roll-over time of not less than 40 years.

## Counter resolution

The counter resolution is a representation of how frequently the counter is updated.

For example, a counter might have an effective frequency of 1GHz, but the actual clock runs at 125MHz and therefore the counter resolution is 125Mhz.

From Armv8.6, Arm recommends the counter resolution is not less than 50MHz in normal running operation.

The counter resolution might vary over time, to accommodate different operating modes of the system such as lower power modes. Such variation might be invisible to the programmer and be system specific, or might be controllable by the programmer through the frequency modes table.

Arm does not specify a required accuracy, but recommends that the counter does not gain or lose more than ten seconds in a 24-hour period.

Use of different counter resolutions must not affect the implemented accuracy.

Starts operating from zero.

The system counter, once configured and running, must provide a uniform view of system time. More precisely, it must be impossible for the following sequence of events to show system time going backwards:

1. Device A reads the time from the system counter.
2. Device A communicates with another agent in the system, Device B.
3. After recognizing the communication from Device A, Device B reads the time from the system counter.

The system counter must be implemented in an always-on power domain.

To support lower-power operating modes in architectures from Armv8.0 to Armv8.5, the counter can operate with a lower counter resolution by incrementing by larger amounts at a lower actual clock frequency. For example, a system counter with an effective frequency of 10MHz might either increment.

- By 1 at 10MHz.
- By 500 at 20kHz, when the system lowers the actual clock frequency, to reduce power consumption.

In this case, the counter must support transitions between higher resolution operation and lower resolution operation, without any impact on the required accuracy of the counter.

From Armv8.6 the counter operates at a fixed effective frequency of 1GHz.

The CNTFRQ register is intended to hold a copy of the effective frequency to allow fast reference to this frequency by software running on the PE. For more information, see Initializing and reading the system effective frequency.

The mechanism by which the count from the system counter is distributed to system components is IMPLEMENTATION DEFINED, but each PE with a System register interface to the system counter must have a counter input that can capture each increment of the counter.

Note

So that the system counter can be clocked independently from the PE hardware, the count value might be distributed using a Gray code sequence. Gray count scheme for timer distribution scheme gives more information about this possibility.

## G6.1.2.1 Initializing and reading the system effective frequency

The CNTFRQ register must be programmed to the effective frequency of the system counter. Typically, this is done only during the system boot process, by using the System register interface to write the system effective frequency to the CNTFRQ register. Only software executing at the highest implemented Exception level can write to CNTFRQ.

Note

The CNTFRQ register is UNKNOWN at reset, and therefore the effective frequency must be set as part of the system boot process.

## Accuracy

## Start-up

Software can read the CNTFRQ register, to determine the effective frequency, in the following states and modes:

- Hyp mode.
- Secure PL1 modes and Non-secure EL1 modes.
- When CNTKCTL.{PL0PCTEN, PL0VCTEN} is not {0,0}, Secure and Non-secure EL0 modes.

## G6.1.2.2 Memory-mapped controls of the system counter

Some system counter controls are accessible only through the memory-mapped interface to the system counter. These controls are:

- Enabling and disabling the counter.
- Setting the counter value.
- Changing the operating mode, to change the counter resolution.
- Enabling Halt-on-debug, which a debugger can then use to suspend counting.

For descriptions of these controls, see System Level Implementation of the Generic Timer.