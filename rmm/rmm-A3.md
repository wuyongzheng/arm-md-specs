## Chapter A3 Realm creation

This section describes the process of creating a Realm.

See also:

- A2.1 Realm
- D1.2 Realm lifecycle flows

## A3.1 Realm feature discovery and selection

- IGJSMC RMMimplementations across different CCA platforms may support disparate features and may offer disparate configuration options for Realms.
- IYRSDX The features supported by an RMI implementation are discovered by reading feature pseudo-register values using the RMI\_FEATURES command.
- XWPHWG The term pseudo-register is used because, although these values are stored in memory, their usage model is similar to feature registers specified in the Arm A-profile architecture.
- IQNJTQ On Realm creation, the Host specifies a set of desired features in a Realm parameters structure to the RMI\_REALM\_CREATE command. The RMM checks that the features specified by the Host are supported by the implementation.
- IRRHJJ The features specified at Realm creation time are included in the Realm Initial Measurement.
- IZHXGX The features supported by an RSI implementation are discovered by reading feature pseudo-register values using the RSI\_FEATURES command.

See also:

- A2.1.6 Realm parameters
- A7.1.1 Realm Initial Measurement
- B4.3.4 RMI\_FEATURES command
- B4.3.9 RMI\_REALM\_CREATE command
- B5.3.3 RSI\_FEATURES command

## A3.1.1 Realm hash algorithm

- IWMKGX The set of hash algorithms supported by the implementation is reported by the RMI\_FEATURES command in RmiFeatureRegister0.
- RKPBQM Requesting an unsupported hash algorithm causes execution of RMI\_REALM\_CREATE to fail.

See also:

- A7.1 Realm measurements
- B4.3.9 RMI\_REALM\_CREATE command
- B4.4.6 RmiFeatureRegister0 type

## A3.1.2 Realm LPA2 and IPA width

- IGVJMZ Support by the implementation for LPA2 is reported by the RMI\_FEATURES command in RmiFeatureRegister0.
- INKLXQ Usage of LPA2 for Realm Translation Tables is an attribute which is set by the Host during Realm creation.
- ILKJGN Realm IPA width is an attribute which is set by the Host during Realm creation.
- RSZVDK Requesting an unsupported IPA width (for example, smaller than the minimum supported, or larger than the maximum supported) causes execution of RMI\_REALM\_CREATE to fail.
- IGKCCS The Host can choose a smaller IPA width than the maximum supported IPA width reported by RMI\_FEATURES. This is true regardless of whether LPA2 is enabled for the Realm.
- XFTVXQ The Host may want to enable LPA2 for a Realm due to either or both of the following reasons:
- to allow the Realm to be configured with a larger IPA width
- to allow access from mappings in the Realm's stage 2 translation to a larger PA space
- IXDBQB A Realm can query its IPA width using the RSI\_REALM\_CONFIG command.

IFSNMG If LPA2 is not enabled for a Realm then passing a PA greater than or equal to 2^48 to any of the following commands causes an error to be returned:

- RMI\_DATA\_CREATE
- RMI\_DATA\_CREATE\_UNKNOWN
- RMI\_RTT\_CREATE
- RMI\_RTT\_MAP\_UNPROTECTED

## See also:

- A5.2.1 Realm IPA space
- B4.3.9 RMI\_REALM\_CREATE command
- B4.4.6 RmiFeatureRegister0 type
- B5.3.9 RSI\_REALM\_CONFIG command

## A3.1.3 Realm support for Scalable Vector Extension

- IKJVLJ Support by the implementation for the Scalable Vector Extension (FEAT\_SVE) is reported by the RMI\_FEATURES command in RmiFeatureRegister0.
- IZJSMJ Availability of SVE to a Realm is set by the Host during Realm creation.
- IVNLNH SVE vector length for a Realm is set by the Host during Realm creation.
- RFZZDS Requesting a larger-than-supported SVE vector length causes execution of RMI\_REALM\_CREATE to fail. This is different from the behaviour of the hardware architecture, in which a larger-than-supported SVE vector length value is silently truncated.
- XYGWTK The RMI ABI provides a natural mechanism to signal an invalid feature selection, via the return code of RMI\_REALM\_CREATE. The analog in the hardware architecture would be to generate an illegal exception return, which would cause undesirable coupling between two disparate parts of the architecture, namely the exception model and the SVE feature.
- RNBYKC If SVE is supported by the platform but is disabled for the Realm via the RMI\_REALM\_CREATE command then a read of ID\_AA64PFR0\_EL1.SVE indicates that SVE is not supported.
- UZRJXL The RMM should trap and emulate reads of ID\_AA64PFR0\_EL1.SVE .
- SVXRNN A Realm should discover SVE support by reading ID\_AA64PFR0\_EL1.SVE rather than based on the platform identity read from MIDR\_EL1 .

See also:

- B4.3.9 RMI\_REALM\_CREATE command
- B4.4.6 RmiFeatureRegister0 type

## A3.1.4 Realm support for self-hosted debug

- ISSTJD Self-hosted debug is always available in Armv8-A.
- ILVMFG The number of breakpoints and watchpoints are attributes which are set by the Host during Realm creation.
- RCJQTB Requesting a number of breakpoints which is larger than the number of breakpoints available causes execution of RMI\_REALM\_CREATE to fail.
- RPLMDH Requesting a number of watchpoints which is larger than the number of watchpoints available causes execution of RMI\_REALM\_CREATE to fail.

See also:

- B4.3.9 RMI\_REALM\_CREATE command

## A3.1.5 Realm support for Performance Monitors Extension

- IRVCQD Support by the implementation for the Performance Monitors Extension (FEAT\_PMU) is reported by the RMI\_FEATURES command in RmiFeatureRegister0.
- INHCFC Availability of PMU to a Realm is set by the Host during Realm creation.
- IXZMKC The number of PMU counters available to a Realm is set by the Host during Realm creation.
- RXVRGD Requesting a number of PMU counters which is larger than the number of PMU counters available causes RMI\_REALM\_CREATE to fail.

See also:

- A8.1 Realm PMU
- B4.3.9 RMI\_REALM\_CREATE command
- B4.4.6 RmiFeatureRegister0 type

## A3.1.6 Realm support for Activity Monitors Extension

- RJJVZS The Activity Monitors Extension (FEAT\_AMUv1) is not available to a Realm.

## A3.1.7

## Realm support for Statistical Profiling Extension

- RDCBNL The Statistical Profiling Extension (FEAT\_SPE) is not available to a Realm.

## A3.1.8 Realm support for Trace Buffer Extension

- RNXDXG The Trace Buffer Extension (FEAT\_TRBE) is not available to a Realm.

## A3.1.9 Number of GICv3 List Registers

- IFLRMX The number of GICv3 List Registers which can be provided by the Host via the RMI\_REC\_ENTER command is reported by the RMI\_FEATURES command in RmiFeatureRegister0.
- XJHNQX Making the number of GICv3 List Registers discoverable via RMI allows the RMM to reserve List Registers for its own usage.

See also:

- B4.3.14 RMI\_REC\_ENTER command
- B4.4.6 RmiFeatureRegister0 type