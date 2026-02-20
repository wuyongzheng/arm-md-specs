## I2.3 Memory-mapped timer components

This part of the Arm Generic Timer specification defines an optional memory-mapped timer component. This can be implemented as part of any programmable system component that does not incorporate a System register mapped Arm Generic Timer, to provide that system component with the timer functionality of an Arm Generic Timer.

The memory map consists of up to eight timer frames . The base address of a frame is CNTBaseN, where N numbers from 0 up to a maximum permitted value of 7.

Each CNTBaseN timer frame:

- Provides its own set of timers and associated interrupts.
- Is implemented in its own memory page or memory protection region.
- Is implemented at a base address, identified as CNTBaseN, that is aligned to the size of the translation granule or memory protection region.

For each implemented CNTBaseN frame the system can optionally provide an unprivileged view of the frame, described as the EL0 view of the frame. The base address of this second view of the CNTBaseN frame is CNTEL0BaseN.

Note In the naming of the registers associated with a CNTBaseN or CNTEL0BaseN frame, the value of N is represented as &lt;n&gt;, for example CNTACR&lt;n&gt;.

If a CNTEL0BaseN frame is implemented:

- Is implemented in its own memory page or memory protection region and is aligned to the size of the translation granule or memory protection region.
- All registers visible in CNTBaseN, except for CNTVOFF and CNTEL0ACR, can be visible in CNTEL0BaseN.
- -Control fields in CNTEL0ACR determine whether each register is visible.
- The offsets of all visible registers are the same as their offsets in the CNTBaseN frame.

In addition to the implemented CNTBaseN and CNTEL0BaseN frames, the system must provide a single control frame at base address CNTCTLBase. CNTCTLBase must be implemented in its own memory page or memory protection region and is aligned to the size of the translation granule or memory protection region.

The system defines the position of each frame in the memory map. This means the values of each of the CNTBaseN, CNTEL0BaseN, and CNTCTLBase base addresses is IMPLEMENTATION DEFINED.

Note

The Arm architecture requires memory-mapped peripherals to be little-endian, and therefore the memory-mapped timers are little-endian.

The following sections describe the implementation of a memory-mapped view of the counter and timer:

- The CNTCTLBase frame.
- The CNTBaseN and CNTEL0BaseN frames.

Note

Providing a complete set of features in a system level implementation gives an implementation example for a system level Generic Timer implementation that provides equivalent features to a System registers Generic Timer implementation in a PE that includes all of the Exception levels.

## I2.3.1 The CNTCTLBase frame

The CNTCTLBase frame contains:

- An identification register for the features of the memory-mapped counter and timer implementation.

- Access controls for each CNTBaseN frame.
- Avirtual offset register for frames that implement a virtual timer.

Table I2-3 shows the CNTCTLBase registers, in order of their offsets from the CNTCTLBase base address.

Note

CNTFRQ and CNTVOFF registers are also implemented in a System register interface to the Generic Timer.

Generic Timer memory-mapped register descriptions describes each of these registers.

## Table I2-3 CNTCTLBase memory map

| Offset        | Register            | Type   | Security a      | Description                                                                                                                                            |
|---------------|---------------------|--------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x000         | CNTFRQ b            | RW     | Restricted      | Counter Frequency register.                                                                                                                            |
| 0x004         | CNTNSAR             | RW     | Restricted      | Counter Non-Secure Access register.                                                                                                                    |
| 0x008         | CNTTIDR             | RO     | No restrictions | Counter Timer ID register.                                                                                                                             |
| 0x00C - 0x03F | -                   | RES0   | -               | Reserved.                                                                                                                                              |
| 0x040 +4 N c  | CNTACR<n>           | RW     | Programmable d  | Counter Access Control register N .                                                                                                                    |
| 0x060 - 0x07F | -                   | RES0   | -               | Reserved.                                                                                                                                              |
| 0x080 +8 N c  | CNTVOFF<n>[31:0] b  | RW e   | Programmable d  | Virtual Offset register N . If the CNTBaseN frame has virtual timer capability then CNTVOFF<n> is implemented as an RWregister, otherwise its location |
| 0x084 +8 N c  | CNTVOFF<n>[63:32] b | RW e   | Programmable d  | is RAZ/WI.                                                                                                                                             |
| 0x0C0 - 0x0FC | -                   | RES0   | -               | Reserved.                                                                                                                                              |
| 0x100 - 0x7FC | -                   | -      | -               | IMPLEMENTATION DEFINED.                                                                                                                                |
| 0x800 - 0xFBC | -                   | RES0   | -               | Reserved.                                                                                                                                              |
| 0xFC0 - 0xFCF | -                   | -      | -               | IMPLEMENTATION DEFINED.                                                                                                                                |
| 0xFD0 - 0xFFC | CounterID<n>        | RO     | No restrictions | Counter ID registers 0-11.                                                                                                                             |

- e. Address is reserved, RAZ/WI if register not implemented.

All implementations of the Generic Timer include the virtual counter. Therefore, conceptually, all implementations include the CNTVOFF register that defines the virtual offset between the physical count and the virtual count. If a memory-mapped Generic Timer component does not distinguish between real time and virtual time, then it can implement CNTVOFF as RAZ/WI. Otherwise CNTVOFF is an RW register, and Arm strongly recommends that the system only permits access to CNTVOFF from EL2 or higher.

## I2.3.2 The CNTBaseN and CNTEL0BaseN frames

Each CNTBaseN frame, or {CNTBaseN, CNTEL0BaseN} pair of frames, provides a memory-mapped counter and timer, see:

- The CNTBaseN frame.
- The CNTEL0BaseN frame.
- CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames.

## I2.3.2.1 The CNTBase N frame

Table I2-4 shows the CNTBaseN registers, in order of their offsets from the CNTBaseN base address. Whether a frame includes a virtual timer is IMPLEMENTATION DEFINED. If it does not, then memory at offsets 0x030 -0x03C is RAZ/WI. Except for CNTEL0ACR and the CounterID&lt;n&gt; registers, equivalent registers are also implemented in a System register interface to the timer component of a Generic Timer.

Generic Timer memory-mapped register descriptions describes each of these registers.

Table I2-4 CNTBaseN memory map

| Offset        | Register           | Type   | Description                                                                                                                                           |
|---------------|--------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x000         | CNTPCT[31:0] a     | RO     | Physical Count register.                                                                                                                              |
| 0x004         | CNTPCT[63:32] a    | RO     |                                                                                                                                                       |
| 0x008         | CNTVCT[31:0] a     | RO     | Virtual Count register.                                                                                                                               |
| 0x00C         | CNTVCT[63:32] a    | RO     |                                                                                                                                                       |
| 0x010         | CNTFRQ a           | RO c   | Counter Frequency register.                                                                                                                           |
| 0x014         | CNTEL0ACR          | RW b   | Counter EL0 Access Control Register, optional in the CNTBaseN memory map.                                                                             |
| 0x018         | CNTVOFF[31:0] a    | RO c   | Virtual Offset register. If CNTVOFF in the CNTCTLBase frame isanRW register, a read of this register returns the value of that register. Otherwise is |
| 0x01C         | CNTVOFF[63:32] a   | RO c   | RAZ.                                                                                                                                                  |
| 0x020         | CNTP_CVAL[31:0] a  | RW     | Physical Timer CompareValue register.                                                                                                                 |
| 0x024         | CNTP_CVAL[63:32] a | RW     |                                                                                                                                                       |
| 0x028         | CNTP_TVAL a        | RW     | Physical TimerValue register.                                                                                                                         |
| 0x02C         | CNTP_CTL a         | RW     | Physical Timer Control register.                                                                                                                      |
| 0x030         | CNTV_CVAL[31:0] a  | RW b   | Virtual Timer CompareValue register, optional in the CNTBaseN memory                                                                                  |
| 0x034         | CNTV_CVAL[63:32] a | RW b   | map.                                                                                                                                                  |
| 0x038         | CNTV_TVAL a        | RW b   | Virtual TimerValue register, optional in the CNTBaseN memory map.                                                                                     |
| 0x03C         | CNTV_CTL a         | RW b   | Virtual Timer Control register, optional in the CNTBaseN memory map.                                                                                  |
| 0x040 - 0xFCF | -                  | RES0   | Reserved.                                                                                                                                             |
| 0xFD0 - 0xFFC | CounterID<n>       | RO     | Counter ID registers 0-11.                                                                                                                            |

## I2.3.2.2 The CNTEL0Base N frame

For any value of N , the layout of the registers in the CNTEL0Base N frame is identical to the CNTBaseN frame, except that, in the CNTEL0Base N frame:

- CNTVOFF is never visible, and the memory at 0x018 -0x01C is RAZ/WI.

- CNTEL0ACR is never visible, and the memory at 0x014 is RAZ/WI.
- If implemented in the CNTBaseN frame, CNTEL0ACR controls whether CNTPCT, CNTVCT, CNTFRQ, the Physical Timer, and the Virtual Timer registers are visible in the CNTEL0BaseN frame. If CNTEL0ACR is not implemented then these registers are not visible in the CNTEL0BaseN frame, and their addresses in that frame are RAZ/WI.

If an implementation supports 64-bit atomic accesses, then CNTPCT, CNTVCT, CNTVOFF, CNTP\_CVAL, and CNTV\_CVAL must be accessible as atomic 64-bit values.

## I2.3.2.3 CNTCTLBase status and control fields for the CNTBase N and CNTEL0Base N frames

In the CNTCTLBase frame:

## CNTTIDR controls:

- Whether each CNTBaseN frame is implemented.
- If a CNTBaseN frame is implemented, whether:
- -That CNTBaseN frame has virtual timer capability.
- -Acorresponding CNTEL0BaseN frame is implemented.

## CNTNSARcontrols:

Whether all the following are accessible by Non-secure accesses and, if FEAT\_RME is implemented, Root accesses and Realm accesses:

- CNTACR&lt;n&gt;.
- CNTVOFF&lt;n&gt;.
- Each implemented CNTBaseN frame, and any corresponding CNTEL0BaseN frame.

## The CNTACR&lt;n&gt; registers control:

For each implemented CNTBaseN frame, the accessibility of the following registers in that frame:

- CNTP\_CTL, CNTP\_CVAL, and CNTP\_TVAL.
- CNTV\_CTL, CNTV\_CVAL, and CNTV\_TVAL.
- CNTVOFF.
- CNTFRQ.
- CNTPCT.
- CNTVCT.

For CNTACR&lt;n&gt;, the value of &lt;n&gt; corresponds to the value of N for the controlled CNTBaseN frame.

## The CNTVOFF&lt;n&gt; registers provide:

For each implemented CNTBaseN frame that has virtual capability, the RW copy of the CNTVOFF register for that frame.

Note

In a CNTBaseN frame that has virtual timer capability the CNTVOFF register is RO.

For CNTVOFF&lt;n&gt;, the value of &lt;n&gt; corresponds to the value of N for the controlled CNTBaseN frame.

## Recommended External Interface to the Performance

## Chapter I3 Monitors

This chapter describes the recommended external interface to the Performance Monitors. It contains the following section:

- About the external interface to the Performance Monitors registers.

Note

Performance Monitors external register descriptions describes the external view of the Performance Monitors registers.