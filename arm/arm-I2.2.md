## I2.2 Memory-mapped counter module

The memory-mapped counter module provides top-level control of the system counter. The CNTControlBase frame holds the registers for the memory-mapped counter, and provides:

- An RW control register, CNTCR, that provides:
- -An enable bit for the system counter.
- -An enable bit for Halt-on-debug. For more information, see Halt-on-debug.
- -Afield that can be written to request a change to the Counter resolution. This mechanism means that, for example, if the Counter resolution is halved then the increment to the counter at each tick of the clock is doubled.

For more information, see Control of counter resolution and increment.

Writes to this register are rare.

- AROstatus register, CNTSR, that provides:
- -Abit that indicates whether the system counter is halted because of an asserted Halt-on-debug signal.
- -Afield that indicates whether a requested change to the Counter resolution has completed.
- Two contiguous 32-bit RW registers that hold the current system counter value, CNTCV. If the system supports 64-bit atomic accesses, these two registers must be accessible by such accesses.

The system counter must be disabled before writing to these registers, otherwise the effect of the write is UNPREDICTABLE.

Writes to these registers are rare.

- A Frequency modes table of one or more 32-bit entries, where:
- -The first entry in the table defines the base frequency of the system counter. It is IMPLEMENTATION DEFINED whether the base frequency indicates the effective frequency of the counter, or the maximum Counter resolution.

Arm recommends that the base frequency indicates the maximum Counter resolution.

- -Each subsequent entry in the table defines an alternative frequency of the system counter, that must be an exact divisor of the base frequency.

A32-bit zero entry immediately follows the last table entry.

This table can be RO or RW. For more information, see The Frequency modes table.

In an implementation with multiple physical address spaces, CNTControlBase is only accessible by accesses from the most secure physical address space. For example, in a system with Secure and Non-secure memory maps, CNTControlBase is only accessible by Secure accesses. For example, in a system with FEAT\_RME, CNTControlBase is only accessible by Root accesses.

In addition, the CNTReadBase frame includes a read-only copy of the system counter value, CNTCV, as two contiguous 32-bit RO registers. If the system supports 64-bit atomic accesses, these two registers must be accessible by such accesses.

Counter module control and status register summary describes CNTReadBase and CNTControlBase memory maps, and the registers in each frame.

## I2.2.1 Control of counter resolution and increment

The system counter has a fixed base frequency , and must maintain the required counter accuracy, meaning Arm recommends that it does not gain or lose more than ten seconds in a 24-hour period, see The system counter. However, the counter can operate at a lower resolution than the base frequency, using a correspondingly larger increment. For example, it can increment by a value four times larger when running at a quarter of the base frequency. Any lower resolution operation, and any switching between resolutions, must not reduce the accuracy of the counter.

Control of the system Counter resolution and increment is provided only through the memory-mapped counter module. The following sections describe this control:

- The Frequency modes table.
- Changing the system counter and increment.

## I2.2.1.1 The Frequency modes table

The Frequency modes table starts at offset 0x20 in the CNTControlBase frame.

Table entries are 32-bits, and each entry specifies a selected frequency, in Hz.

The first entry in the table specifies the base frequency of the system counter.

When the system counter is operating at a lower frequency than the base frequency, the increment applied at each counter update is increased by the ratio of the base frequency and the selected frequency.

Note

Where the Effective frequency and the base frequency are not the same, the increment is not solely defined by the ratio of the base frequency and the selected frequency. For example, a counter with an Effective frequency of 1GHz and a base frequency of 125MHz will increment by a value of 8 on each tick of the base frequency. If the Frequency modes table provides an additional selected frequency of 31.25MHz, then when this frequency is selected the counter increments by 32 on each tick of the selected frequency.

A32-bit word of zero value marks the end of the table. That is, the word of memory immediately after the last entry in the table must be zero.

The only required entry in the table is the entry for the base frequency.

Typically, the Frequency modes table is in RO memory. However, a system implementation might use RW memory for the table, and initialize the table entries as part of its startup sequence. Therefore, the CNTControlBase memory map shows the table region as RO or RW.

Arm strongly recommends that the Frequency modes table is not updated once the system is running.

The architecture can support up to 1004 entries in the Frequency modes table, including the zero-word end marker, and the number of entries is IMPLEMENTATION DEFINED, up to this limit.

Note

- Arm considers it likely that implementations will require significantly fewer entries than the architectural limit.
- In the CNTControlBase frame, the offset range 0x0C0 -0x0FC can be used for IMPLEMENTATION DEFINED registers. If any registers are defined in this space, then the Frequency modes table cannot extend beyond offset 0x0B8 , with a zero word at offset 0x0BC . This means that if any IMPLEMENTATION DEFINED registers are defined the maximum number of entries in the table is 40, including the zero-word end marker.

## I2.2.1.2 Changing the system counter and increment

The value of the CNTCR.FCREQ field specifies which entry in the Frequency modes table specifies the selected frequency.

Changing the value of CNTCR.FCREQ requests a change to the selected frequency. To ensure the frequency change does not affect the overall accuracy of the counter, a change is made as follows:

- When changing from a higher frequency to a lower frequency, the counter:
1. Continues running at the higher frequency until the count reaches an integer multiple of the required lower frequency.

2. Switches to operating at the lower frequency.
- When changing from a lower frequency to a higher frequency, the counter:
1. Waits until the end of the current lower-frequency cycle.
2. Makes the counter increment required for operation at that lower frequency.
3. Switches to operating at the higher frequency.

When the frequency has changed, CNTSR is updated to indicate the new selected frequency. Therefore, a system component that is waiting for a frequency change can poll CNTSR to detect the change.

## I2.2.2 Halt-on-debug

The CNTCR register provides an enable bit for an OPTIONAL Halt-on-debug signal.

When the CNTCR.HDBG bit is set to 1, and the Halt-on-debug signal is implemented and asserted, the system counter is halted. Otherwise, the system counter ignores the state of this signal.

Where the system counter implements a Halt-on-debug signal and the system supports halting the system counter, Arm recommends that the Halt-on-debug signal can be controlled by a debugger using the Embedded Cross-Trigger (ECT) using a system-level cross-trigger interface that includes:

- Adebug request output trigger event that asserts the Halt-on-debug signal.
- Arestart request output trigger event that deasserts the Halt-on-debug signal.

For more information, see About the Embedded Cross-Trigger.

Note

Software must use the Halt-on-debug enable bit to ensure that the timers cannot be halted maliciously in an attempt to prohibit progress.

For more information about Halt-on-debug, contact Arm.

## I2.2.3 Counter module control and status register summary

The Counter module control and status registers are memory-mapped registers in the following register memory frames :

- Acontrol frame, with base address CNTControlBase.
- Astatus frame, with base address CNTReadBase.

Each of these register memory frames is in its own memory page or memory protection region, and the frame base address points to the start of this region. Each base address must be aligned to the size of the translation granule or protection granule.

Note

Each frame of a memory-mapped Generic Timer takes the name of its base address.

In each register memory frame, the memory at offset 0xFD0 - 0xFFF is reserved for twelve 32-bit IMPLEMENTATION DEFINED ID registers, see the CounterID&lt;n&gt; register descriptions for more information.

Note

The Arm architecture requires memory-mapped peripherals to be little-endian, and therefore the counter is little-endian.

In an implementation with multiple physical address spaces, CNTControlBase is only accessible by accesses from the most secure physical address space. For example, in a system with Secure and Non-secure memory maps, CNTControlBase is only accessible by Secure accesses. For example, in a system with FEAT\_RME, CNTControlBase is only accessible by Root accesses.

Table I2-1 shows the CNTControlBase control registers, in order of their offsets from the CNTControlBase base address, for an implementation that includes registers in the IMPLEMENTATION DEFINED register space 0x0C0 -0x0FC , and also has

fewer than 39 CNTFID&lt;n&gt; registers. The Frequency modes table describes how this memory map differs if more CNTFID&lt;n&gt; registers are implemented.

Generic Timer memory-mapped register descriptions describes each of these registers.

Table I2-1 CNTControlBase memory map

| Offset                | Name         | Type                   | Description                                                                          |
|-----------------------|--------------|------------------------|--------------------------------------------------------------------------------------|
| 0x000                 | CNTCR        | RW                     | Counter Control Register.                                                            |
| 0x004                 | CNTSR        | RO                     | Counter Status Register.                                                             |
| 0x008                 | CNTCV[31:0]  | RW                     | Counter Count Value register.                                                        |
| 0x00C                 | CNTCV[63:32] | RW                     |                                                                                      |
| 0x010                 | CNTSCR a     | RW                     | Counter Scale Register.                                                              |
| 0x014 - 0x018         | -            | RES0                   | Reserved.                                                                            |
| 0x01C                 | CNTID a      | RO                     | Counter Identification Register.                                                     |
| 0x020                 | CNTFID0      | ROorRW                 | Frequency modes table, and end marker. For more information, see The Frequency modes |
| 0x020 +4 n            | CNTFID<n>    | ROorRW                 | table.                                                                               |
| 0x024 +4 n            | -            | ROor RW,RAZ            |                                                                                      |
| ( 0x028 +4 n )- 0x0BC | -            | RO, RES0               | Reserved.                                                                            |
| 0x0C0 - 0x0FC         | -            | IMPLEMENTATION DEFINED | Reserved for IMPLEMENTATION DEFINED registers.                                       |
| 0x100 - 0xFCC         | -            | RO, RES0               | Reserved.                                                                            |
| 0xFD0 - 0xFFC         | CounterID<n> | RO                     | Counter ID registers 0-11.                                                           |

Table I2-2 shows the CNTReadBase control registers, in order of their offsets from the CNTReadBase base address. Generic Timer memory-mapped register descriptions describes each of these registers.

Table I2-2 CNTReadBase memory map

| Offset        | Name         | Type   | Description                  |
|---------------|--------------|--------|------------------------------|
| 0x000         | CNTCV[31:0]  | RO     | Counter Count Value register |
| 0x004         | CNTCV[63:32] | RO     |                              |
| 0x008 - 0xFCC | -            | RES0   | Reserved                     |
| 0xFD0 - 0xFFC | CounterID<n> | RO     | Counter ID registers 0-11    |