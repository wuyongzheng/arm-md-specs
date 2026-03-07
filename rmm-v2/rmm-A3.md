## Chapter A3 Feature discovery and configuration

This section describes how the Host discovers features which are supported by the RMM implementation, and how the Host configures the features which are used by or available to a Realm.


## A3.1 Feature discovery and configuration overview

- RMMimplementations across different CCA platforms may support disparate features and may offer disparate configuration options for Realms.
- The features supported by an RMI implementation are discovered by reading feature pseudo-register values using the RMI\_FEATURES command.
- The term pseudo-register is used because, although these values are stored in memory, their usage model is similar to feature registers specified in the Arm A-profile architecture.
- On Realm creation, the Host provides a desired configuration in a Realm parameters structure to the RMI\_REALM\_CREATE command. The RMM checks that the configuration provided by the Host is supported by the implementation.
- Aspects of the Realm configuration which affect the security posture of the Realm are included in the Realm Initial Measurement.
- The features supported by an RSI implementation are discovered by reading feature pseudo-register values using the RSI\_FEATURES command.

See also:

- [A2.2.6 Realm parameters](rmm-A2.2.md#a226-realm-parameters)
- [A7.1.1 Realm Initial Measurement](rmm-A7.1.md#a711-realm-initial-measurement)
- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.14 RMI\_FEATURES command](rmm-B4.5.14.md)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B5.4.4 RSI\_FEATURES command](rmm-B5.4.4.md)
- [C2.19 RmmGlobalStatic type](rmm-C2.md#c219-rmmglobalstatic-type)

## A3.2 Realm hash algorithm

- The set of hash algorithms supported by the implementation is reported by the RMI\_FEATURES command in RmiFeatureRegister1.
- The hash algorithm used by a Realm is provided by the Host when calling RMI\_REALM\_CREATE.


- Providing an unsupported hash algorithm causes execution of RMI\_REALM\_CREATE to fail.

See also:

- [A7.1 Realm measurements](rmm-A7.1.md)
- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.27 RmiFeatureRegister1 type](rmm-B4.6.md#b4627-rmifeatureregister1-type)

## A3.3 Realm LPA2 and IPA width

- Support by the implementation for LPA2 is reported by the RMI\_FEATURES command in RmiFeatureRegister0::LPA2.
- Usage of LPA2 for Realm Translation Tables is configured by the Host when calling RMI\_REALM\_CREATE.
- Realm IPA width is provided by the Host when calling RMI\_REALM\_CREATE.
- Providing an unsupported IPA width (for example, smaller than the minimum supported, or larger than the maximum supported) causes execution of RMI\_REALM\_CREATE to fail.
- The Host can choose a smaller IPA width than the maximum supported IPA width reported by RMI\_FEATURES. This is true regardless of whether LPA2 is enabled for the Realm.

- The Host may want to enable LPA2 for a Realm due to either or both of the following reasons:
- to allow the Realm to be configured with a larger IPA width
- to allow access from mappings in the Realm's stage 2 translation to a larger PA space
- A Realm can query its IPA width using the RSI\_REALM\_CONFIG command.
- If LPA2 is not enabled for a Realm then passing a PA greater than or equal to 2^48 to any of the following commands causes an error to be returned:
- RMI\_RTT\_DATA\_MAP\_INIT
- RMI\_RTT\_DATA\_MAP
- RMI\_RTT\_CREATE
- RMI\_RTT\_AUX\_CREATE
- RMI\_RTT\_UNPROT\_MAP

See also:

- [A5.2.1 Realm IPA space](rmm-A5.1.md#a521-realm-ipa-space)
- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.26 RmiFeatureRegister0 type](rmm-B4.6.md#b4626-rmifeatureregister0-type)
- [B5.4.16 RSI\_REALM\_CONFIG command](rmm-B5.4.16.md)
- A3.4 Realm support for Scalable Vector Extension IKJVLJ Support by the implementation for the Scalable Vector Extension (FEAT\_SVE) is reported by the RMI\_FEATURES command in RmiFeatureRegister1::SVE. IZJSMJ Availability of SVE to a Realm is configured by the Host when calling RMI\_REALM\_CREATE. IVNLNH SVE vector length for a Realm is provided by the Host when calling RMI\_REALM\_CREATE. RFZZDS Providing a larger-than-supported SVE vector length causes execution of RMI\_REALM\_CREATE to fail. This is different from the behaviour of the hardware architecture, in which a larger-than-supported SVE vector length value is silently truncated.
- The RMI ABI provides a natural mechanism to signal an invalid feature selection, via the return code of RMI\_REALM\_CREATE. The analog in the hardware architecture would be to generate an illegal exception return, which would cause undesirable coupling between two disparate parts of the architecture, namely the exception model and the SVE feature.
- Providing a larger-than-supported SVE vector length causes execution of RMI\_REALM\_CREATE to fail prepares the architecture for addition of Realm live migration support in future. Assuming that the live migration flow starts with creation of an empty destination Realm, configured identically to the source Realm, this provides a point where the necessary feature support can be checked on the destination platform.
- If SVE is supported by the platform but is disabled for the Realm via the RMI\_REALM\_CREATE command then a read of ID\_AA64PFR0\_EL1.SVE indicates that SVE is not supported.
- The RMM should trap and emulate reads of ID\_AA64PFR0\_EL1.SVE .
- A Realm should discover SVE support by reading ID\_AA64PFR0\_EL1.SVE rather than based on the platform identity read from MIDR\_EL1 .

See also:

- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.27 RmiFeatureRegister1 type](rmm-B4.6.md#b4627-rmifeatureregister1-type)

## A3.5 Realm support for self-hosted debug

- Self-hosted debug is always available in Armv8-A.
- The number of breakpoints and watchpoints available are reported by the RMI\_FEATURES command in RmiFeatureRegister0::{NUM\_BPS,NUM\_WPS}.
- The number of breakpoints and watchpoints are provided by the Host when calling RMI\_REALM\_CREATE.
- Providing a number of breakpoints which is larger than the number of breakpoints available causes execution of RMI\_REALM\_CREATE to fail.
- Providing a number of watchpoints which is larger than the number of watchpoints available causes execution of RMI\_REALM\_CREATE to fail.
- Specifying that a larger-than-supported number of breakpoints or watchpoints causes execution of RMI\_REALM\_CREATE to fail prepares the architecture for addition of Realm live migration support in future. Assuming that the live migration flow starts with creation of an empty destination Realm, configured identically to the source Realm, this provides a point where the necessary feature support can be checked on the destination platform.

See also:

- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.26 RmiFeatureRegister0 type](rmm-B4.6.md#b4626-rmifeatureregister0-type)

## A3.6 Realm support for Performance Monitors Extension

- Support by the implementation for the Performance Monitors Extension (FEAT\_PMU) is reported by the RMI\_FEATURES command in RmiFeatureRegister0::PMU.
- Availability of PMU to a Realm is configured by the Host when calling RMI\_REALM\_CREATE.
- The number of PMU counters available to a Realm is provided by the Host when calling RMI\_REALM\_CREATE.
- Providing a number of PMU counters which is larger than the number of PMU counters available causes RMI\_REALM\_CREATE to fail.


- Specifying that a larger-than-supported number of PMU counters causes RMI\_REALM\_CREATE to fail prepares the architecture for addition of Realm live migration support in future. Assuming that the live migration flow starts with creation of an empty destination Realm, configured identically to the source Realm, this provides a point where the necessary feature support can be checked on the destination platform.

See also:

- [A8.1 Realm PMU](rmm-A8.md#a81-realm-pmu)
- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.26 RmiFeatureRegister0 type](rmm-B4.6.md#b4626-rmifeatureregister0-type)

## A3.7 Realm support for Activity Monitors Extension

- The Activity Monitors Extension (FEAT\_AMUv1) is not available to a Realm.

## A3.8 Realm support for Statistical Profiling Extension


The Statistical Profiling Extension (FEAT\_SPE) is not available to a Realm.

## A3.9 Realm support for Trace Buffer Extension

- The Trace Buffer Extension (FEAT\_TRBE) is not available to a Realm.

## A3.10 Support for Realm device assignment

- Support by the implementation for Realm device assignment is reported by the RMI\_FEATURES command in RmiFeatureRegister2::DA.
- Availability of Realm device assignment for a Realm is configured by the Host when calling RMI\_REALM\_CREATE. See also:
- Chapter A9 Realm device assignment
- B3.101 RealmParamsSupported function
- B4.5.46 RMI\_REALM\_CREATE command
- B4.6.28 RmiFeatureRegister2 type

## A3.11 Support for coherent memory devices

- I0002 Support by the implementation for coherent memory devices is reported by the RMI\_FEATURES command in RmiFeatureRegister2::DA\_COH.
- I0003 The maximum number of coherent memory devices is reported by the RMI\_FEATURES command in RmiFeatureRegister2::MAX\_CMEM.
- I0004 Whether the platform requires Target-Side Encryption (TSE) in coherent memory devices is reported by the RMI\_FEATURES command in RmiFeatureRegister2::CMEM\_TSE\_REQ.

See also:

- [A9.11 Coherent memory devices](rmm-A9.11.md)
- [B4.6.28 RmiFeatureRegister2 type](rmm-B4.6.md#b4628-rmifeatureregister2-type)


## A3.12 Support for auxiliary Planes

- The maximum number of auxiliary Planes supported by the implementation is reported by the RMI\_FEATURES command in of RmiFeatureRegister3::MAX\_NUM\_AUX\_PLANED.
- The maximum number of auxiliary Planes supported by the implementation is either 0 or 3.
- The number of auxiliary Planes for a Realm is provided by the Host when calling RMI\_REALM\_CREATE.
- Providing a number of auxiliary Planes which is larger than the maximum number of auxiliary Planes causes RMI\_REALM\_CREATE to fail.
- For a Realm with a non-zero number of auxiliary Planes, the RmiFeatureRegister3::RTT\_PLANE field indicates which one of the following configurations is supported by the implementation:
- The Realm has an RTT tree per Plane
- The Realm has a single RTT tree
- The Realm can be configured to either have an RTT tree per Plane, or a single RTT tree.

Whether a Realm has an RTT tree per Plane is configured by the Host when calling RMI\_REALM\_CREATE.

## See also:

- [Chapter A10 Planes](rmm-A9.11.md#chapter-a10-planes)


- [B3.101 RealmParamsSupported function](rmm-B3.md#b3101-realmparamssupported-function)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.29 RmiFeatureRegister3 type](rmm-B4.6.md#b4629-rmifeatureregister3-type)
- [C2.19 RmmGlobalStatic type](rmm-C2.md#c219-rmmglobalstatic-type)

## A3.13 Support for Stage 2 Access Permissions indirect encoding

- The RmiFeatureRegister3::RTT\_S2AP\_INDIRECT field indicates whether the Stage 2 Access Permissions (S2AP) value for a Realm IPA is:
- Encoded directly in the RTT entry, or
- Encoded indirectly, as described in 'Stage 2 Indirect permissions' in Arm Architecture Reference Manual for A-Profile architecture [3].
- Whether a Realm uses S2AP indirect encoding is configured by the Host when calling RMI\_REALM\_CREATE.
- See also:
- Arm Architecture Reference Manual for A-Profile architecture [3]
- A5.6.11 Stage 2 Access Permissions
- B3.101 RealmParamsSupported function
- B4.5.46 RMI\_REALM\_CREATE command
- B4.6.29 RmiFeatureRegister3 type
- C2.19 RmmGlobalStatic type

## A3.14 Live Firmware Activation

- Live Firmware Activation (LFA) allows an update to a platform firmware component to be activated without rebooting the system. This potentially includes components which are within the TCB of a Realm.
- A Realm has an LFA policy which is provided by the Host when calling RMI\_REALM\_CREATE.
- If the LFA policy of a Realm is LFA\_DISALLOW then all firmware components within the Realm's TCB are guaranteed not to be live activated during the lifetime of the Realm.
- In order to apply LFA to any firmware component (including the RMM) which is within the TCB of a Realm whose LFA policy is LFA\_DISALLOW, the Host must first destroy the Realm.


- The mechanism via which the LFA implementation determines whether any Realm with an LFA policy of LFA\_DISALLOW currently exists on the system is IMPLEMENTATION DEFINED.
- If the LFA policy of a Realm is LFA\_DISALLOW then the contents of the CCA platform software components claim reflect the state of all firmware components within the Realm's TCB, throughout the lifetime of the Realm.
- The LFA policy of a Realm is reflected in the Realm attestation token.

See also:

- Live Firmware Activation SMC Interface [5]
- [A7.2.3.3.8 CCA platform software components claim](rmm-A7.2.3.3.md#a72338-cca-platform-software-components-claim)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [B4.6.36 RmiLfaPolicy type](rmm-B4.6.md#b4636-rmilfapolicy-type)

## A3.15 Support for Realm memory encryption

- A Realm has an MEC policy which is provided by the Host when calling RMI\_REALM\_CREATE.

A MEC policy describes whether the Realm's memory encryption context is:

Chapter A3. Feature discovery and configuration A3.15. Support for Realm memory encryption

- Shared with other Realms
- Private to the Realm

See also:

- [A7.2.3.1 Realm claims](rmm-A7.2.3.1.md)
- [Chapter A11 Realm memory encryption](rmm-A11.md)

<!-- image -->