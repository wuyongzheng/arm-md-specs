## I5.7 Generic Timer memory-mapped register descriptions

This section describes the Generic Timer registers. Generic Timer memory-mapped registers overview gives an overview of these registers, and includes links to their memory maps.

## I5.7.1 CNTACR&lt;n&gt;, Counter-timer Access Control Registers, n = 0 - 7

The CNTACR&lt;n&gt; characteristics are:

## Purpose

Provides top-level access controls for the elements of a timer frame. CNTACR&lt;n&gt; provides the controls for frame CNTBaseN.

In addition to the CNTACR&lt;n&gt; control:

- CNTNSARcontrols whether CNTACR&lt;n&gt; is accessible by Non-secure accesses.
- If frame CNTEL0BaseN is implemented, the CNTEL0ACR in frame CNTBaseN provides additional control of accesses to frame CNTEL0BaseN.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTACR&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

Implemented only if the value of CNTTIDR.Frame&lt;n&gt; is 1.

An implementation of the counters might not provide configurable access to some or all of the features. In this case, the associated field in the CNTACR&lt;n&gt; register is:

- RAZ/WI if access is always denied.
- RAO/WI if access is always permitted.

## Attributes

CNTACR&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:6]

Reserved, RES0.

## RWPT, bit [5]

Read/write access to the EL1 Physical Timer registers CNTP\_CVAL, CNTP\_TVAL, and CNTP\_CTL, in frame &lt;n&gt;.

| RWPT   | Meaning                                                                             |
|--------|-------------------------------------------------------------------------------------|
| 0b0    | No access to the EL1 Physical Timer registers in frame <n>. The registers are RES0. |
| 0b1    | Read/write access to the EL1 Physical Timer registers in frame <n>.                 |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## RWVT, bit [4]

Read/write access to the Virtual Timer register CNTV\_CV AL, CNTV\_TVAL, and CNTV\_CTL, in frame &lt;n&gt;.

| RWVT   | Meaning                                                                        |
|--------|--------------------------------------------------------------------------------|
| 0b0    | No access to the Virtual Timer registers in frame <n>. The registers are RES0. |
| 0b1    | Read/write access to the Virtual Timer registers in frame <n>.                 |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## RVOFF, bit [3]

Read-only access to CNTVOFF, in frame &lt;n&gt;.

| RVOFF   | Meaning                                                  |
|---------|----------------------------------------------------------|
| 0b0     | No access to CNTVOFF in frame <n>. The register is RES0. |
| 0b1     | Read-only access to CNTVOFF in frame <n>.                |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## RFRQ, bit [2]

Read-only access to CNTFRQ, in frame &lt;n&gt;.

| RFRQ   | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0    | No access to CNTFRQ in frame <n>. The register is RES0. |
| 0b1    | Read-only access to CNTFRQ in frame <n>.                |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## RVCT, bit [1]

Read-only access to CNTVCT, in frame &lt;n&gt;.

| RVCT   | Meaning                                                |
|--------|--------------------------------------------------------|
| 0b0    | No access to CNTVCTin frame <n>. The register is RES0. |
| 0b1    | Read-only access to CNTVCTin frame <n>.                |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## RPCT, bit [0]

Read-only access to CNTPCT, in frame &lt;n&gt;.

| RPCT   | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0    | No access to CNTPCT in frame <n>. The register is RES0. |
| 0b1    | Read-only access to CNTPCT in frame <n>.                |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTACR&lt;n&gt;

In a system that supports the Realm Management Extension, CNTNSAR.NS&lt;n&gt; describes how these registers can be accessed by Root or Realm accesses.

In a system that recognizes two Security states:

- CNTACR&lt;n&gt; is always accessible by Secure accesses.
- CNTNSAR.NS&lt;n&gt; determines whether CNTACR&lt;n&gt; is accessible by Non-secure accesses.

CNTACR&lt;n&gt; can be accessed through the memory-mapped interface:

| Component   | Frame      | Offset          | Instance   |
|-------------|------------|-----------------|------------|
| Timer       | CNTCTLBase | 0x040 + (4 * n) | CNTACR<n>  |

Accesses to this register are RW.

## I5.7.2 CNTCR, Counter Control Register

The CNTCR characteristics are:

## Purpose

Enables the counter, controls the counter resolution, and controls counter behavior during debug.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTCR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## FCREQ, bits [17:8]

Frequency change request. Indicates the number of the entry in the Frequency modes table to select.

Selecting an unimplemented entry, or an entry that contains 0, has no effect on the counter.

The maximum number of entries in the Frequency modes table is IMPLEMENTATION DEFINED up to a maximum of 1004 entries, see 'The Frequency modes table'. An implementation is only required to implement an FCREQ field that can hold values from 0 to the highest supported Frequency modes table entry. Any unrequired most-significant bits of FCREQ can be implemented as RES0.

The reset behavior of this field is:

- On a Timer reset, this field resets to '0000000000' .

## Bits [7:3]

Reserved, RES0.

## SCEN, bit [2]

## When FEAT\_CNTSC is implemented:

Scale Enable.

| SCEN   | Meaning                                                                                         |
|--------|-------------------------------------------------------------------------------------------------|
| 0b0    | Scaling is not enabled. The counter value is incremented by 0x1 .0000000 for each counter tick. |

0b1

Scaling is enabled. The counter is incremented by CNTSCR.ScaleVal for each counter tick.

The SCEN bit can only be changed when the counter is disabled, when CNTCR.EN == 0.

If the value of CNTCR.SCEN changes when CNTCR.EN == 1, then:

- The counter value becomes UNKNOWN.
- The counter value remains UNKNOWN on future ticks of the clock.

When the CNTCV register in the CNTControlBase frame of the memory mapped counter module is written to, the accumulated fraction information is reset to zero.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## HDBG, bit [1]

Halt-on-debug. Controls whether a Halt-on-debug signal halts the system counter:

| HDBG   | Meaning                                                    |
|--------|------------------------------------------------------------|
| 0b0    | System counter ignores Halt-on-debug.                      |
| 0b1    | Asserted Halt-on-debug signal halts system counter update. |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## EN, bit [0]

Enables the counter:

The reset behavior of this field is:

- On a Timer reset, this field resets to '0' .

## Accessing CNTCR

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes this register, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes this register, is implemented only in the Secure physical address space.

CNTCRcan be accessed through the memory-mapped interface:

| EN   | Meaning                  |
|------|--------------------------|
| 0b0  | System counter disabled. |
| 0b1  | System counter enabled.  |

| Component   | Frame          | Offset   | Instance   |
|-------------|----------------|----------|------------|
| Timer       | CNTControlBase | 0x000    | CNTCR      |

Accesses to this register are RW.

## I5.7.3 CNTCV, Counter Count Value register

The CNTCV characteristics are:

## Purpose

Indicates the current count value.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTCV is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTCVis a 64-bit register.

## Field descriptions

<!-- image -->

| 63         | 32         |            |
|------------|------------|------------|
| CountValue | CountValue | CountValue |
| 31         | 0          |            |
| CountValue | CountValue | CountValue |

## CountValue, bits [63:0]

Indicates the counter value.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTCV

| Frame          | Accessibility   |
|----------------|-----------------|
| CNTControlBase | RW              |
| CNTReadBase    | RO              |

Awrite to CNTCV must be visible in the CNTPCT register of each running processor in a finite time.

For the instance of the register in the CNTControlBase frame:

- In a system that supports the Realm Management Extension, this register is implemented only in the Root physical address space.
- In a system that supports Secure and Non-secure physical address spaces, this register is implemented only in the Secure physical address space.
- If the counter is enabled, the effect of writing to the register is UNKNOWN.

For the instance of the register in the CNTReadBase frame, this register is accessible in all physical address spaces.

In an implementation that supports 64-bit atomic memory accesses, this register must be accessible using a 64-bit atomic access.

CNTCVcan be accessed through the memory-mapped interface:

| Component   | Frame          | Offset   | Instance   | Range   |
|-------------|----------------|----------|------------|---------|
| Timer       | CNTControlBase | 0x008    | CNTCV      | 63:0    |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTReadBase | 0x000    | CNTCV      | 63:0    |

Accesses to this register are RO.

## I5.7.4 CNTEL0ACR, Counter-timer EL0 Access Control Register

The CNTEL0ACR characteristics are:

## Purpose

An implementation of CNTEL0ACR in the frame at CNTBaseN controls whether the CNTPCT, CNTVCT, CNTFRQ, EL1 Physical Timer, and Virtual Timer registers are visible in the frame at CNTEL0BaseN.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTEL0ACR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

Implementation of this register is OPTIONAL.

## Attributes

CNTEL0ACR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:10]

Reserved, RES0.

## EL0PTEN, bit [9]

Second view read/write access control for the EL1 Physical Timer registers. This bit controls whether the CNTP\_CVAL, CNTP\_TVAL, and CNTP\_CTL registers in the current CNTBaseN frame are also accessible in the corresponding CNTEL0BaseN frame.

| EL0PTEN   | Meaning                                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------|
| 0b0       | No access. Registers are RES0 in the second view.                                                                    |
| 0b1       | Access permitted. If the registers are accessible in the current frame, then they are accessible in the second view. |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## EL0VTEN, bit [8]

Second view read/write access control for the Virtual Timer registers. This bit controls whether the CNTV\_CV AL, CNTV\_TVAL, and CNTV\_CTL registers in the current CNTBaseN frame are also accessible in the corresponding CNTEL0BaseN frame.

| EL0VTEN   | Meaning                                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------|
| 0b0       | No access. Registers are RES0 in the second view.                                                                    |
| 0b1       | Access permitted. If the registers are accessible in the current frame, then they are accessible in the second view. |

The definition of this bit means that, if the Virtual Timer registers are not implemented in the current CNTBaseN frame, then the Virtual Timer register addresses are RES0 in the corresponding CNTEL0BaseN frame, regardless of the value of this bit.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Bits [7:2]

Reserved, RES0.

## EL0VCTEN, bit [1]

Second view read access control for CNTVCT and CNTFRQ.

| EL0VCTEN   | Meaning                                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------|
| 0b0        | CNTVCTis not visible in the second view. If EL0PCTEN is set to 0, CNTFRQ is not visible in the second view.       |
| 0b1        | Access permitted. If CNTVCTand CNTFRQ are visible in the current frame, then they are visible in the second view. |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## EL0PCTEN, bit [0]

Second view read access control for CNTPCT and CNTFRQ.

| EL0PCTEN   | Meaning                                                                                                            |
|------------|--------------------------------------------------------------------------------------------------------------------|
| 0b0        | CNTPCT is not visible in the second view. If EL0VCTEN is set to 0, CNTFRQ is not visible in the second view.       |
| 0b1        | Access permitted. If CNTPCT and CNTFRQ are visible in the current frame, then they are visible in the second view. |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTEL0ACR

CNTEL0ACR can be implemented in any implemented CNTBaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

If CNTEL0ACR is not implemented in an implemented CNTBaseN frame:

- The register location in that frame is RAZ/WI.
- If the corresponding CNTEL0BaseN frame is implemented, the registers CNTFRQ, CNTP\_CTL, CNTP\_CVAL, CNTP\_TVAL, CNTPCT, CNTV\_CTL, CNTV\_CVAL, CNTV\_TVAL, and CNTVCT are not visible and accesses are RAZ/WI in that frame.

CNTEL0ACR can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x014    | CNTEL0ACR  |

Accesses to this register are RW.

## I5.7.5 CNTFID0, Counter Frequency ID

The CNTFID0 characteristics are:

## Purpose

Indicates the base frequency of the system counter.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTFID0 is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

The possible frequencies for the system counter are stored in the Frequency modes table as 32-bit words starting with the base frequency, CNTFID0. For more information, see 'The Frequency modes table'.

The final entry in the Frequency modes table must be followed by a 32-bit word of zero value, to mark the end of the table.

Typically, the Frequency modes table will be in read-only memory. However, a system implementation might use read/write memory for the table, and initialize the table entries as part of its start-up sequence.

If the Frequency modes table is in read/write memory, Arm strongly recommends that the table is not updated once the system is running.

## Attributes

CNTFID0 is a 32-bit register.

## Field descriptions

| 31        | 0   |
|-----------|-----|
| Frequency |     |

## Frequency, bits [31:0]

The base frequency of the system counter, in Hz.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTFID0

It is IMPLEMENTATION DEFINED whether this register is RO or RW

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes this register, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes this register, is implemented only in the Secure physical address space.

CNTFID0 can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset   | Instance   |
|-------------|----------------|----------|------------|
| Timer       | CNTControlBase | 0x020    | CNTFID0    |

Accesses to this register are IMPLEMENTATION DEFINED.

## I5.7.6 CNTFID&lt;n&gt;, Counter Frequency IDs, n &gt; 0, n = 1 - 1003

The CNTFID&lt;n&gt; characteristics are:

## Purpose

Indicates alternative system counter frequencies.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTFID&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

The possible frequencies for the system counter are stored in the Frequency modes table as 32-bit words starting with the base frequency, CNTFID0, see 'The Frequency modes table'.

The number of CNTFID&lt;n&gt; registers is IMPLEMENTATION DEFINED, and the only required CNTFID&lt;n&gt; register is CNTFID0.

The final entry in the Frequency modes table must be followed by a 32-bit word of zero value, to mark the end of the table.

The architecture can support up to 1004 entries in the Frequency modes table, including the zero-word end marker, and the number of entries is IMPLEMENTATION DEFINED up to this limit. For an implementation that includes registers in the IMPLEMENTATION DEFINED register space 0x0C0 -0x0FC , the maximum number of entries in the Frequency modes table is 40, including the zero-word end marker.

Typically, the Frequency modes table will be in read-only memory. However, a system implementation might use read/write memory for the table, and initialize the table entries as part of its start-up sequence.

If the Frequency modes table is in read/write memory, Arm strongly recommends that the table is not updated once the system is running.

## Attributes

CNTFID&lt;n&gt; is a 32-bit register.

## Field descriptions

Frequency

31

0

<!-- image -->

## Frequency, bits [31:0]

Asystem counter frequency, in Hz. Must be an exact divisor of the base frequency. Arm strongly recommends that all frequency values in the Frequency modes table are integer power-of-two divisors of the base frequency.

When the system timer is operating at a lower frequency than the base frequency, the increment applied at each counter update is increased by the ratio of the base frequency and the selected frequency.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTFID&lt;n&gt;

It is IMPLEMENTATION DEFINED whether this register is RO or RW

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes these registers, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes these registers, is implemented only in the Secure physical address space.

CNTFID&lt;n&gt; can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset          | Instance   |
|-------------|----------------|-----------------|------------|
| Timer       | CNTControlBase | 0x020 + (4 * n) | CNTFID<n>  |

Accesses to this register are IMPLEMENTATION DEFINED.

## I5.7.7 CNTFRQ, Counter-timer Frequency

The CNTFRQ characteristics are:

## Purpose

This register is provided so that software can discover the effective frequency of the system counter. The instance of the register in the CNTCTLBase frame must be programmed with this value as part of system initialization. The value of the register is not interpreted by hardware.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTFRQ is implemented in the Core power domain or in the Debug power domain

For more information see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTFRQ is a 32-bit register.

## Field descriptions

<!-- image -->

## ClockFreq, bits [31:0]

Clock frequency. Indicates the effective frequency of the system counter, in Hz.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTFRQ

CNTFRQ must be implemented as an RW register in the CNTCTLBase frame.

In a system that supports the Realm Management Extension, the instance of the register in the CNTCTLBase frame is accessible as follows:

- For Root accesses, it is IMPLEMENTATION DEFINED whether accesses to the register are permitted or behave as RES0.
- For Realm accesses, this register behaves as RES0.

In a system that recognizes two Security states, the instance of the register in the CNTCTLBase frame is only accessible by Secure accesses.

CNTFRQ can be implemented as a RO register in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTFRQ is accessible in that frame, as a RO register, if the value of CNTACR&lt;n&gt;.RFRQ is 1.
- Otherwise, the CNTFRQ address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTFRQ is accessible as a RO register in that frame if both:
- CNTFRQ is accessible in the corresponding CNTBaseN frame.
- Either the value of CNTEL0ACR.EL0VCTEN is 1 or the value of CNTEL0ACR.EL0PCTEN is 1.
- Otherwise, the CNTFRQ address in that frame is RAZ/WI.

CNTFRQ can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x010    | CNTFRQ     |

Accesses to this register are RO.

| Component   | Frame       | Offset   | Instance   |
|-------------|-------------|----------|------------|
| Timer       | CNTEL0BaseN | 0x010    | CNTFRQ     |

Accesses to this register are RO.

| Component   | Frame      | Offset   | Instance   |
|-------------|------------|----------|------------|
| Timer       | CNTCTLBase | 0x000    | CNTFRQ     |

Accesses to this register are RO.

## I5.7.8 CNTID, Counter Identification Register

The CNTID characteristics are:

## Purpose

Indicates whether counter scaling is implemented.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTID is implemented in the Core power domain or in the Debug power domain

This register is present only when FEAT\_CNTSC is implemented. Otherwise, direct accesses to CNTID are RES0.

## Attributes

CNTID is a 32-bit register.

## Field descriptions

<!-- image -->

| 31   | 4 3   |
|------|-------|
|      | CNTSC |

## Bits [31:4]

Reserved, RES0.

## CNTSC, bits [3:0]

Indicates whether Counter Scaling is implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CNTSC   | Meaning                             |
|---------|-------------------------------------|
| 0b0000  | Counter scaling is not implemented. |
| 0b0001  | Counter scaling is implemented.     |

All other values are reserved.

Access to this field is RO.

## Accessing CNTID

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes this register, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes this register, is implemented only in the Secure physical address space.

CNTID can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset   | Instance   |
|-------------|----------------|----------|------------|
| Timer       | CNTControlBase | 0x1C     | CNTID      |

Accesses to this register are RO.

## I5.7.9 CNTNSAR, Counter-timer Non-secure Access Register

The CNTNSAR characteristics are:

## Purpose

Provides the highest-level control of whether frames CNTBaseN and CNTEL0BaseN are accessible by Non-secure accesses.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTNSAR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTNSARis a 32-bit register.

## Field descriptions

| 31   | 7 6 5 4 3 2 1 0   |
|------|-------------------|

## Bits [31:8]

Reserved, RES0.

## NS&lt;n&gt; , bits [n], for n = 7 to 0

Non-secure access to frame n.

| NS<n>   | Meaning                                                                                                                                                                                                                                                            |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | Secure access only. Behaves as RES0 to Non-secure accesses. If FEAT_RME is implemented, it is IMPLEMENTATION DEFINED whether Root accesses to the specified registers are permitted or behave as RES0. For Realm accesses, the specified registers behave as RES0. |
| 0b1     | Secure and Non-secure accesses permitted. If FEAT_RME is implemented, it is IMPLEMENTATION DEFINED whether Root and Realm accesses to the specified registers are permitted. If not permitted, the specified registers behave as RES0 for Root and Realm accesses. |

This bit also determines whether, in the CNTCTLBase frame, CNTACR&lt;n&gt; and CNTVOFF&lt;n&gt; are accessible to Non-secure accesses.

If frame CNTBase&lt;n&gt;:

- Is not implemented, then NS&lt;n&gt; is RES0.
- Is not Configurable access, and is accessible only by Secure accesses, then NS&lt;n&gt; is RES0.
- Is not Configurable access, and is accessible by both Secure and Non-secure accesses, then NS&lt;n&gt; is RES1.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTNSAR

In a system that supports the Realm Management Extension, this register is accessible as follows:

- For Root accesses, it is IMPLEMENTATION DEFINED whether accesses to the register are permitted or behave as RES0.
- For Realm accesses, this register behaves as RES0.

In a system that recognizes two Security states, this register is only accessible by Secure accesses.

CNTNSARcan be accessed through the memory-mapped interface:

| Component   | Frame      | Offset   | Instance   |
|-------------|------------|----------|------------|
| Timer       | CNTCTLBase | 0x004    | CNTNSAR    |

Accesses to this register are RW.

## I5.7.10 CNTP\_CTL, Counter-timer Physical Timer Control

The CNTP\_CTL characteristics are:

## Purpose

Control register for the EL1 physical timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTP\_CTL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTP\_CTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0, then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTP\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_CTL

CNTP\_CTL can be implemented in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTP\_CTL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWPT is 1.
- Otherwise, the CNTP\_CTL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTP\_CTL is accessible in that frame if both:
- CNTP\_CTL is accessible in the corresponding CNTBaseN frame:
- The value of CNTEL0ACR.EL0PTEN is 1.
- Otherwise, the CNTP\_CTL address in that frame is RAZ/WI.

CNTP\_CTL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x02C    | CNTP_CTL   |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   |
|-------------|-------------|----------|------------|
| Timer       | CNTEL0BaseN | 0x02C    | CNTP_CTL   |

Accesses to this register are RW.

## I5.7.11 CNTP\_CVAL, Counter-timer Physical Timer CompareValue

The CNTP\_CVAL characteristics are:

## Purpose

Holds the 64-bit compare value for the EL1 physical timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTP\_CVAL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTP\_CVAL is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the EL1 physical timer CompareValue.

When CNTP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTP\_CTL.ISTATUS is set to 1.
- An interrupt is generated if CNTP\_CTL.IMASK is 0.

When CNTP\_CTL.ENABLE is 0, the timer condition is not met, but CNTPCT continues to count.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_CVAL

CNTP\_CVAL can be implemented in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTP\_CVAL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWPT is 1.
- Otherwise, the CNTP\_CVAL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTP\_CVAL is accessible in that frame if both:
- CNTP\_CVAL is accessible in the corresponding CNTBaseN frame:
- The value of CNTEL0ACR.EL0PTEN is 1.
- Otherwise, the CNTP\_CVAL address in that frame is RAZ/WI.

If the implementation supports 64-bit atomic accesses, then the CNTP\_CV AL register must be accessible as an atomic 64-bit value.

CNTP\_CVAL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x020    | CNTP_CVAL  | 31:0    |

Accesses to this register are RW.

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x024    | CNTP_CVAL  | 63:32   |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x020    | CNTP_CVAL  | 31:0    |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x024    | CNTP_CVAL  | 63:32   |

Accesses to this register are RW.

## I5.7.12 CNTP\_TVAL, Counter-timer Physical Timer TimerValue

The CNTP\_TVAL characteristics are:

## Purpose

Holds the timer value for the EL1 physical timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTP\_TVAL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTP\_TVAL is a 32-bit register.

## Field descriptions

TimerValue

31

0

<!-- image -->

## TimerValue, bits [31:0]

The TimerValue view of the EL1 physical timer.

On a read of this register:

- If CNTP\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTP\_CTL.ENABLE is 1, the value returned is (CompareValue - CNTPCT).

On a write of this register, CompareValue is set to (CNTPCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTP\_CTL.ENABLE is 1, the timer condition is met when (CNTPCT - CompareValue) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTP\_CTL.ISTATUS is set to 1.
- If CNTP\_CTL.IMASK is 0, an interrupt is generated.

When CNTP\_CTL.ENABLE is 0, the timer condition is not met, but CNTPCT continues to count, so the TimerValue view appears to continue to count down.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTP\_TVAL

CNTP\_TVAL can be implemented in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.

- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTP\_TVAL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWPT is 1.
- Otherwise, the CNTP\_TVAL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTP\_TVAL is accessible in that frame if both:
- CNTP\_TVAL is accessible in the corresponding CNTBaseN frame:
- The value of CNTEL0ACR.EL0PTEN is 1.
- Otherwise, the CNTP\_TVAL address in that frame is RAZ/WI.

CNTP\_TVAL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x028    | CNTP_TVAL  |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   |
|-------------|-------------|----------|------------|
| Timer       | CNTEL0BaseN | 0x028    | CNTP_TVAL  |

Accesses to this register are RW.

## I5.7.13 CNTPCT, Counter-timer Physical Count

The CNTPCT characteristics are:

## Purpose

Holds the 64-bit physical count value.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTPCT is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTPCT is a 64-bit register.

## Field descriptions

<!-- image -->

## PhysicalCount, bits [63:0]

Physical count value.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTPCT

CNTPCT can be implemented in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame, as a RO register.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTPCT is accessible in that frame, as a RO register, if the value of CNTACR&lt;n&gt;.RPCT is 1.
- Otherwise, the CNTPCT address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTPCT is accessible in that frame if both:
- CNTPCT is accessible in the corresponding CNTBaseN frame.

- The value of CNTEL0ACR.EL0PCTEN is 1.
- Otherwise, the CNTPCT address in that frame is RAZ/WI.

If the implementation supports 64-bit atomic accesses, then the CNTPCT register must be accessible as an atomic 64-bit value.

CNTPCT can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x000    | CNTPCT     | 31:0    |

Accesses to this register are RO.

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x004    | CNTPCT     | 63:32   |

Accesses to this register are RO.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x000    | CNTPCT     | 31:0    |

Accesses to this register are RO.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x004    | CNTPCT     | 63:32   |

Accesses to this register are RO.

## I5.7.14 CNTSCR, Counter Scale Register

The CNTSCR characteristics are:

## Purpose

Enables the counter, controls the counter effective frequency setting, and controls counter behavior during debug.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTSCR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

This register is present only when FEAT\_CNTSC is implemented. Otherwise, direct accesses to CNTSCR are RES0.

## Attributes

CNTSCR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31       | 0   |
|----------|-----|
| ScaleVal |     |

## ScaleVal, bits [31:0]

Scale Value

When counter scaling is enabled, ScaleVal is the average amount added to the counter value for one period of the frequency of the Generic counter as described in the CNTFRQ register.

The actual rate of update of the counter value is determined by the counter resolution.

ScaleVal is expressed as an unsigned fixed point number with an 8-bit integer value and a 24-bit fractional value.

CNTSCR.ScaleVal can only be changed when CNTCR.EN == 0. If the value of this field is changed when CNTCR.EN == 1:

- The counter value becomes UNKNOWN.
- The counter value remains UNKNOWN on future ticks of the clock.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTSCR

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes this register, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes this register, is implemented only in the Secure physical address space.

CNTSCR can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset   | Instance   |
|-------------|----------------|----------|------------|
| Timer       | CNTControlBase | 0x10     | CNTSCR     |

Accesses to this register are RW.

## I5.7.15 CNTSR, Counter Status Register

The CNTSR characteristics are:

## Purpose

Provides counter resolution status information.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTSR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTSR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:18]

Reserved, RES0.

## FCACK, bits [17:8]

Frequency Change Acknowledge. Indicates the currently selected entry in the Frequency modes table, see 'The Frequency modes table'.

The reset behavior of this field is:

- On a Timer reset, this field resets to '0000000000' .

## Bits [7:2]

Reserved, RES0.

## DBGH, bit [1]

Indicates whether the counter is halted because the Halt-on-debug signal is asserted:

| DBGH   | Meaning                |
|--------|------------------------|
| 0b0    | Counter is not halted. |
| 0b1    | Counter is halted.     |

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Bit [0]

Reserved, RES0.

## Accessing CNTSR

In a system that supports the Realm Management Extension, the CNTControlBase frame, which includes this register, is implemented only in the Root physical address space.

In a system that supports Secure and Non-secure physical address spaces, the CNTControlBase frame, which includes this register, is implemented only in the Secure physical address space.

CNTSR can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset   | Instance   |
|-------------|----------------|----------|------------|
| Timer       | CNTControlBase | 0x004    | CNTSR      |

Accesses to this register are RO.

## I5.7.16 CNTTIDR, Counter-timer Timer ID Register

The CNTTIDR characteristics are:

## Purpose

Indicates the implemented timers in the physical address space, and their features. For each value of N from 0 to 7 it indicates whether:

- Frame CNTBaseN is a view of an implemented timer.
- Frame CNTBaseN has a second view, CNTEL0BaseN.
- Frame CNTBaseN has a virtual timer capability.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTTIDR is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTTIDR is a 32-bit register.

## Field descriptions

| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7    | 4 3    | 0   |
|--------|---------|---------|---------|---------|---------|--------|--------|-----|
| Frame7 | Frame6  | Frame5  | Frame4  | Frame3  | Frame2  | Frame1 | Frame0 |     |

## Frame&lt;n&gt; , bits [4n+3:4n], for n = 7 to 0

A4-bit field indicating the features of frame CNTBase&lt;n&gt;.

Bit[3] of the field is RES0.

Bit[2], the FEL0 subfield, indicates whether frame CNTBase&lt;n&gt; has a second view, CNTEL0Base&lt;n&gt;. The possible values of this bit are:

| Bit[2]   | Meaning                                                                                              |
|----------|------------------------------------------------------------------------------------------------------|
| 0b0      | Frame<n> does not have a second view. The CNTEL0ACR register in the first view of the frame is RES0. |
| 0b1      | Frame<n> has a second view, CNTEL0Base<n>.                                                           |

If bit[0] is 0, bit[2] is RES0.

Bit[1], the FVI subfield, indicates whether both:

- Frame CNTBase&lt;n&gt; implements the virtual timer registers CNTV\_CVAL, CNTV\_TVAL, and CNTV\_CTL.
- This CNTCTLBase frame implements the virtual timer offset register CNTVOFF&lt;n&gt;.

The possible values of bit[1] are:

| Bit[1]   | Meaning                                                                                    |
|----------|--------------------------------------------------------------------------------------------|
| 0b0      | Frame<n> does not have virtual capability. The virtual time and offset registers are RES0. |
| 0b1      | Frame<n> has virtual capability. The virtual time and offset registers are implemented.    |

If bit[0] is 0, bit[1] is RES0.

Bit[0], the FI subfield, indicates whether frame CNTBase&lt;n&gt; is implemented. The possible values of this bit are:

| Bit[0]   | Meaning                                                                        |
|----------|--------------------------------------------------------------------------------|
| 0b0      | Frame<n> is not implemented. All registers associated with the frame are RES0. |
| 0b1      | Frame<n> is implemented.                                                       |

## Accessing CNTTIDR

In a system that supports the Realm Management Extension, it is IMPLEMENTATION DEFINED whether Root and Realm accesses to this register are permitted. If not permitted, this register behaves as RES0 for Root and Realm accesses.

In a system that recognizes two Security states, this register is accessible by both Secure and Non-secure accesses.

CNTTIDR can be accessed through the memory-mapped interface:

| Component   | Frame      | Offset   | Instance   |
|-------------|------------|----------|------------|
| Timer       | CNTCTLBase | 0x008    | CNTTIDR    |

Accesses to this register are RO.

## I5.7.17 CNTV\_CTL, Counter-timer Virtual Timer Control

The CNTV\_CTL characteristics are:

## Purpose

Control register for the virtual timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTV\_CTL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTV\_CTL is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:3]

Reserved, RES0.

## ISTATUS, bit [2]

The status of the timer. This bit indicates whether the timer condition is met:

| ISTATUS   | Meaning                     |
|-----------|-----------------------------|
| 0b0       | Timer condition is not met. |
| 0b1       | Timer condition is met.     |

When the value of the ENABLE bit is 1, ISTATUS indicates whether the timer condition is met. ISTATUS takes no account of the value of the IMASK bit. If the value of ISTATUS is 1 and the value of IMASK is 0, then the timer interrupt is asserted.

When the value of the ENABLE bit is 0, the ISTATUS field is UNKNOWN.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

Access to this field is RO.

## IMASK, bit [1]

Timer interrupt mask bit. Permitted values are:

| IMASK   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | Timer interrupt is not masked by the IMASK bit. |
| 0b1     | Timer interrupt is masked by the IMASK bit.     |

For more information, see the description of the ISTATUS bit.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## ENABLE, bit [0]

Enables the timer. Permitted values are:

| ENABLE   | Meaning         |
|----------|-----------------|
| 0b0      | Timer disabled. |
| 0b1      | Timer enabled.  |

Setting this bit to 0 disables the timer output signal, but the timer value accessible from CNTV\_TV AL continues to count down.

Note

Disabling the output signal might be a power-saving option.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_CTL

CNTV\_CTL can be implemented in any implemented CNTBaseN frame that has virtual timer capability, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame that has virtual timer capability:

- CNTV\_CTL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWVT is 1.
- Otherwise, the CNTV\_CTL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTV\_CTL is accessible in that frame if both:
- CNTV\_CTL is accessible in the corresponding CNTBaseN frame:
- The value of CNTEL0ACR.EL0VTEN is 1.
- Otherwise, the CNTV\_CTL address in that frame is RAZ/WI.

CNTV\_CTL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x03C    | CNTV_CTL   |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   |
|-------------|-------------|----------|------------|
| Timer       | CNTEL0BaseN | 0x03C    | CNTV_CTL   |

Accesses to this register are RW.

## I5.7.18 CNTV\_CVAL, Counter-timer Virtual Timer CompareValue

The CNTV\_CVAL characteristics are:

## Purpose

Holds the 64-bit compare value for the virtual timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTV\_CVAL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTV\_CVAL is a 64-bit register.

## Field descriptions

<!-- image -->

## CompareValue, bits [63:0]

Holds the virtual timer CompareValue.

When CNTV\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CompareValue) is greater than or equal to zero. This means that CompareValue acts like a 64-bit upcounter timer. When the timer condition is met:

- CNTV\_CTL.ISTATUS is set to 1.
- An interrupt is generated if CNTV\_CTL.IMASK is 0.

When CNTV\_CTL.ENABLE is 0, the timer condition is not met, but CNTVCT continues to count.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_CVAL

CNTV\_CVAL can be implemented in any implemented CNTBaseN frame that has virtual timer capability, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame that has virtual timer capability:

- CNTV\_CVAL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWVT is 1.
- Otherwise, the CNTV\_CVAL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTV\_CVAL is accessible in that frame if both:
- CNTV\_CVAL is accessible in the corresponding CNTBaseN frame:
- The value of CNTEL0ACR.EL0VTEN is 1.
- Otherwise, the CNTV\_CVAL address in that frame is RAZ/WI.

If the implementation supports 64-bit atomic accesses, then the CNTV\_CV AL register must be accessible as an atomic 64-bit value.

CNTV\_CVAL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x030    | CNTV_CVAL  | 31:0    |

Accesses to this register are RW.

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x034    | CNTV_CVAL  | 63:32   |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x030    | CNTV_CVAL  | 31:0    |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x034    | CNTV_CVAL  | 63:32   |

Accesses to this register are RW.

## I5.7.19 CNTV\_TVAL, Counter-timer Virtual Timer TimerValue

The CNTV\_TVAL characteristics are:

## Purpose

Holds the timer value for the virtual timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTV\_TVAL is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTV\_TVAL is a 32-bit register.

## Field descriptions

TimerValue

31

0

<!-- image -->

## TimerValue, bits [31:0]

The TimerValue view of the virtual timer.

On a read of this register:

- If CNTV\_CTL.ENABLE is 0, the value returned is UNKNOWN.
- If CNTV\_CTL.ENABLE is 1, the value returned is (CompareValue - CNTVCT).

On a write of this register, CompareValue is set to (CNTVCT + TimerValue), where TimerValue is treated as a signed 32-bit integer.

When CNTV\_CTL.ENABLE is 1, the timer condition is met when (CNTVCT - CompareValue) is greater than or equal to zero. This means that TimerValue acts like a 32-bit downcounter timer. When the timer condition is met:

- CNTV\_CTL.ISTATUS is set to 1.
- If CNTV\_CTL.IMASK is 0, an interrupt is generated.

When CNTV\_CTL.ENABLE is 0, the timer condition is not met, but CNTVCT continues to count, so the TimerValue view appears to continue to count down.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTV\_TVAL

CNTV\_TVAL can be implemented in any implemented CNTBaseN frame that has virtual timer capability, and in the corresponding CNTEL0BaseN frame.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.

- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame that has virtual timer capability:

- CNTV\_TVAL is accessible in that frame if the value of CNTACR&lt;n&gt;.RWVT is 1.
- Otherwise, the CNTV\_TVAL address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTV\_TVAL is accessible in that frame if both:
- CNTV\_TVAL is accessible in the corresponding CNTBaseN frame.
- The value of CNTEL0ACR.EL0VTEN is 1.
- Otherwise, the CNTV\_TVAL address in that frame is RAZ/WI.

CNTV\_TVAL can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   |
|-------------|----------|----------|------------|
| Timer       | CNTBaseN | 0x038    | CNTV_TVAL  |

Accesses to this register are RW.

| Component   | Frame       | Offset   | Instance   |
|-------------|-------------|----------|------------|
| Timer       | CNTEL0BaseN | 0x038    | CNTV_TVAL  |

Accesses to this register are RW.

## I5.7.20 CNTVCT, Counter-timer Virtual Count

The CNTVCT characteristics are:

## Purpose

Holds the 64-bit virtual count value.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTVCT is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTVCTis a 64-bit register.

## Field descriptions

<!-- image -->

## VirtualCount, bits [63:0]

Virtual count value.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVCT

CNTVCTcan be implemented in any implemented CNTBaseN frame, and in the corresponding CNTEL0BaseN frame, as a RO register.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame:

- CNTVCTis accessible in that frame, as a RO register, if the value of CNTACR&lt;n&gt;.RVCT is 1.
- Otherwise, the CNTVCT address in that frame is RAZ/WI.

For an implemented CNTEL0BaseN frame:

- CNTVCTis accessible in that frame if both:
- CNTVCTis accessible in the corresponding CNTBaseN frame.

- The value of CNTEL0ACR.EL0VCTEN is 1.
- Otherwise, the CNTVCT address in that frame is RAZ/WI.

If the implementation supports 64-bit atomic accesses, then the CNTVCT register must be accessible as an atomic 64-bit value.

CNTVCTcan be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x008    | CNTVCT     | 31:0    |

Accesses to this register are RO.

| Component   | Frame    | Offset   | Instance   | Range   |
|-------------|----------|----------|------------|---------|
| Timer       | CNTBaseN | 0x00C    | CNTVCT     | 63:32   |

Accesses to this register are RO.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x008    | CNTVCT     | 31:0    |

Accesses to this register are RO.

| Component   | Frame       | Offset   | Instance   | Range   |
|-------------|-------------|----------|------------|---------|
| Timer       | CNTEL0BaseN | 0x00C    | CNTVCT     | 63:32   |

Accesses to this register are RO.

## I5.7.21 CNTVOFF, Counter-timer Virtual Offset

The CNTVOFF characteristics are:

## Purpose

Holds the 64-bit virtual offset for a CNTBaseN frame that has virtual timer capability. This is the offset between real time and virtual time.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTVOFF is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

## Attributes

CNTVOFF is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| Virtual offset | Virtual offset | Virtual offset |
| 31             | 0              |                |
| Virtual offset | Virtual offset | Virtual offset |

## VOffset, bits [63:0]

Virtual offset.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVOFF

CNTVOFF is implemented, as a RO register, in any implemented CNTBaseN frame that has virtual timer capability.

'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a CNTBaseN frame is implemented, and for an implemented frame:

- Whether the CNTBaseN frame has virtual timer capability.
- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

For an implemented CNTBaseN frame that has virtual timer capability:

- CNTVOFF is accessible in that frame, as a RO register, if the value of CNTACR&lt;n&gt;.RVOFF is 1.
- Otherwise, the CNTVOFF address in that frame is RAZ/WI.

Note

CNTVOFF is never visible in any CNTEL0BaseN frame. This means that the CNTVOFF address in any implemented CNTEL0BaseN frame is RAZ/WI.

In an implementation that supports 64-bit atomic accesses, then the CNTVOFF register must be accessible as an atomic 64-bit value.

CNTVOFF can be accessed through the memory-mapped interface:

| Component   | Frame    | Offset   | Range   |
|-------------|----------|----------|---------|
| Timer       | CNTBaseN | 0x018    | 31:0    |

Accesses to this register are RO.

| Component   | Frame    | Offset   | Range   |
|-------------|----------|----------|---------|
| Timer       | CNTBaseN | 0x01C    | 63:32   |

Accesses to this register are RO.

## I5.7.22 CNTVOFF&lt;n&gt;, Counter-timer Virtual Offsets, n = 0 - 7

The CNTVOFF&lt;n&gt; characteristics are:

## Purpose

Holds the 64-bit virtual offset for frame CNTBase&lt;n&gt;. This is the offset between real time and virtual time.

## Configuration

It is IMPLEMENTATION DEFINED whether CNTVOFF&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

Implementation of this register is OPTIONAL.

## Attributes

CNTVOFF&lt;n&gt; is a 64-bit register.

## Field descriptions

<!-- image -->

| 63             | 32             |                |
|----------------|----------------|----------------|
| Virtual offset | Virtual offset | Virtual offset |
| 31             | 0              |                |
| Virtual offset | Virtual offset | Virtual offset |

## VOffset, bits [63:0]

Virtual offset.

The reset behavior of this field is:

- On a Timer reset, this field resets to an architecturally UNKNOWN value.

## Accessing CNTVOFF&lt;n&gt;

In the CNTCTLBase frame a CNTVOFF&lt;n&gt; register must be implemented, as a RW register, for each CNTBaseN frame that has virtual timer capability. For more information, see 'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames'.

Note

The value of &lt;n&gt; in an instance of CNTVOFF&lt;n&gt; specifies the value of N for the associated CNTBaseN frame.

In a system that supports the Realm Management Extension, CNTNSAR.NS&lt;n&gt; describes how these registers can be accessed by Root or Realm accesses.

In a system that recognizes two Security states, for any CNTVOFF&lt;n&gt; register in the CNTCTLBase frame:

- CNTVOFF&lt;n&gt; is always accessible by Secure accesses.
- CNTNSAR.NS&lt;n&gt; determines whether CNTVOFF&lt;n&gt; is accessible by Non-secure accesses.

The register location of any unimplemented CNTVOFF&lt;n&gt; register in the CNTCTLBase frame is RAZ/WI.

The CNTVOFF&lt;n&gt; register is accessible in the CNTBaseN frame using CNTVOFF.

In an implementation that supports 64-bit atomic accesses, then the CNTVOFF&lt;n&gt; registers must be accessible as atomic 64-bit values.

CNTVOFF&lt;n&gt; can be accessed through the memory-mapped interface:

| Component   | Frame      | Offset   |    |      | Range   |
|-------------|------------|----------|----|------|---------|
| Timer       | CNTCTLBase | 0x080 n) | +  | (8 * | 31:0    |

Accesses to this register are RW.

| Component   | Frame      | Offset   |    |    |    | Range   |
|-------------|------------|----------|----|----|----|---------|
| Timer       | CNTCTLBase | 0x084 n) | +  | (8 | *  | 63:32   |

Accesses to this register are RW.

## I5.7.23 CounterID&lt;n&gt;, Counter ID registers, n = 0 - 11

The CounterID&lt;n&gt; characteristics are:

## Purpose

IMPLEMENTATION DEFINED identification registers 0 to 11 for the memory-mapped Generic Timer.

## Configuration

It is IMPLEMENTATION DEFINED whether CounterID&lt;n&gt; is implemented in the Core power domain or in the Debug power domain

For more information, see 'Power and reset domains for the system level implementation of the Generic Timer'.

These registers are implemented independently in each of the implemented Generic Timer memory-mapped frames.

If the implementation of the Counter ID registers requires an architecture version, the value for this version of the Arm Generic Timer is version 0.

The Counter ID registers can be implemented as a set of CoreSight ID registers, comprising Peripheral ID Registers and Component ID Registers. An implementation of these registers for the Generic Timer must use a Component class value of 0xF .

## Attributes

CounterID&lt;n&gt; is a 32-bit register.

## Field descriptions

<!-- image -->

## IMPLEMENTATIONDEFINED, bits [31:0]

IMPLEMENTATION DEFINED.

## Accessing CounterID&lt;n&gt;

These registers must be implemented, as RO registers, in every implemented Generic Timer memory-mapped frame.

For the CNTCTLBase frame, in a system that supports the Realm Management Extension, it is IMPLEMENTATION DEFINED whether Root and Realm accesses to these registers are permitted. If not permitted, these registers behave as RES0 for Root and Realm accesses.

For the CNTCTLBase frame, in a system that recognizes two Security states these registers are accessible by both Secure and Non-secure accesses.

For the CNTControlBase frame, in a system that supports the Realm Management Extension, the frame is implemented only in the Root physical address space, meaning these registers are implemented only in the Root physical address space.

For the CNTControlBase frame, in a system that supports Secure and Non-secure physical address spaces, the frame is implemented only in the Secure physical address space, meaning these registers are implemented only in the Secure physical address space.

For the CNTReadBase frame, these registers are accessible in all physical address spaces.

For the CNTBaseN frames, 'CNTCTLBase status and control fields for the CNTBaseN and CNTEL0BaseN frames' describes the status fields that identify whether a frame is implemented, and for an implemented frame:

· Whether the CNTBaseN frame has virtual timer capability.

- Whether the corresponding CNTEL0BaseN frame is implemented.
- For an implementation that supports the Realm Management Extension, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Root and Realm accesses.
- For an implementation that recognizes two Security states, whether the CNTBaseN frame, and any corresponding CNTEL0BaseN frame, is accessible by Non-secure accesses. The CNTBaseN frame is always accessible by Secure accesses.

CounterID&lt;n&gt; can be accessed through the memory-mapped interface:

| Component   | Frame          | Offset     | Instance     |
|-------------|----------------|------------|--------------|
| Timer       | CNTControlBase | 0xFD0 + n) | CounterID<n> |

Accesses to this register are RO.

| Component   | Frame       | Offset          | Instance     |
|-------------|-------------|-----------------|--------------|
| Timer       | CNTReadBase | 0xFD0 + (4 * n) | CounterID<n> |

Accesses to this register are RO.

| Component   | Frame    | Offset        | Instance     |
|-------------|----------|---------------|--------------|
| Timer       | CNTBaseN | 0xFD0 + (4 n) | CounterID<n> |

Accesses to this register are RO.

| Component   | Frame       | Offset          | Instance     |
|-------------|-------------|-----------------|--------------|
| Timer       | CNTEL0BaseN | 0xFD0 + (4 * n) | CounterID<n> |

Accesses to this register are RO.

| Component   | Frame      | Offset          | Instance     |
|-------------|------------|-----------------|--------------|
| Timer       | CNTCTLBase | 0xFD0 + (4 * n) | CounterID<n> |

Accesses to this register are RO.