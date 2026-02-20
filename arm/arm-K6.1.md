## K6.1 Providing a complete set of features in a system level implementation

As an example system design, using memory-mapped Generic Timer components as described in System Level Implementation of the Generic Timer, the feature set of a System registers counter and timer, in an implementation that includes Non-secure EL2 and EL3, can be implemented using the following set of timer frames:

- ACNTCTLBase control frame.
- The following CNTBase N timer frames:

- Frame 0 Accessible by Non-secure accesses, with second view and virtual capability. This provides the Non-secure EL1&amp;0 timers.

- Frame 1 Accessible by Non-secure accesses, with no second view and no virtual capability. This provides the Non-secure EL2 timers.

- Frame 2 Accessible only by Secure accesses, with a second view but no virtual capability. This provides the Secure PL1&amp;0 timers, meaning:

- Compared to a PE where EL3 is using AArch64, it provides the Secure EL1&amp;0 timer.

- Compared to a PE where EL3 is using AArch32, it provides the only Secure state timer.

- Frame 3 Accessible only by Secure accesses, with no second view and no virtual capability. This provides the EL3 timers.

Note

This frame is not required for a memory-mapped timer that provides only the feature set of a PE for which EL3 is using AArch32.

In this implementation, the full set of implemented frames, and accessibility as memory pages in the different translation regimes, is as follows:

## CNTCTLBase

## CNTEL0Base0

The control frame. This frame is accessible in both the Secure and Non-secure memory maps, and:

- In the Secure EL1&amp;0 translation regime, this frame is accessible only at EL1.
- In the Non-secure EL2 translation regime, this frame is accessible.
- In the Non-secure EL1&amp;0 translation regime, this frame is not accessible.
- CNTBase0 The first view of the Non-secure EL1&amp;0 timers. This frame is accessible only in the Non-secure memory map, and:
- In the Secure EL1&amp;0 translation regime, this frame is accessible only at EL1.
- In the Non-secure EL2 translation regime, this frame is accessible.
- In the Non-secure EL1&amp;0 translation regime, this frame is accessible only at EL1.

The second view of CNTBase0, meaning it is the EL0 view of the Non-secure EL1&amp;0 timers. This frame is accessible only in the Non-secure memory map, and:

- In the Secure EL1&amp;0 translation regime, the architecture permits this frame to be accessible at EL1, or at EL1 and EL0, but does not require either of these options.
- In the Non-secure EL2 translation regime, this frame is accessible.
- In the Non-secure EL1&amp;0 translation regime, this frame is accessible at EL1 and EL0.
- CNTBase1 The first and only view of the Non-secure EL2 timers. This frame is accessible only in Non-secure memory map, and:
- When EL3 is using AArch64:
- -In the Secure EL1&amp;0 translation regime, this frame is accessible only at EL1.
- -In the EL3 translation regime, this frame is accessible.

## CNTEL0Base2

- When EL3 is using AArch32, in the Secure PL1&amp;0 translation regime, this frame is accessible only at PL1 (EL3).
- In the Non-secure EL2 translation regime, this frame is accessible.
- In the Non-secure EL1&amp;0 translation regime, this frame is not accessible.

CNTBase2 The first view of the Secure EL1&amp;0, or PL1&amp;0 timers.

Note

In AArch64 state, these timers are always called the Secure EL1&amp;0 timers. In AArch32 state they are usually called the Secure PL1&amp;0 timers because, in AArch32 Secure state, whether some of the PE modes map to EL1 or to EL3 depends on whether EL3 is using AArch64 or AArch32. See Security state, Exception levels, and AArch32 execution privilege.

This frame is accessible only in the Secure memory map, and:

- When EL3 is using AArch64:
- -In the Secure EL1&amp;0 translation regime, this frame is accessible only at EL1.
- -In the EL3 translation regime, this frame is accessible.
- When EL3 is using AArch32, in the Secure PL1&amp;0 translation regime, this frame is accessible only at PL1 (EL3).
- Because the frame is in Secure memory, it is not accessible in any Non-secure translation regime.

The second view of CNTBase2, meaning it is the EL0 view of the Secure EL1&amp;0, or PL1&amp;0, timers.

Note

See the Note in the description of the CNTBase2 frame for more information about the naming of these timers.

This frame is accessible only in the Secure memory map, and:

- When EL3 is using AArch64:
- -In the Secure EL1&amp;0 translation regime, this frame is accessible at EL1 and EL0.
- -In the EL3 translation regime, this frame is accessible.
- When EL3 is using AArch32, in the Secure PL1&amp;0 translation regime, this frame is accessible at PL1 (EL3) and EL0.
- Because the frame is in Secure memory, it is not accessible in any Non-secure translation regime.

CNTBase3 The first and only view of the EL3 timers. This frame is accessible only in the Secure memory map, and:

- When EL3 is using AArch64:
- -In the Secure EL1&amp;0 translation regime, this frame is not accessible.
- -In the EL3 translation regime, this frame is accessible.
- When EL3 is using AArch32, this frame is not accessible.
- Because the frame is in Secure memory, it is not accessible in any Non-secure translation regime.