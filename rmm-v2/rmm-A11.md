## Chapter A11 Realm memory encryption

This section describes encryption of physical memory which is accessible via Realm PAS. This encryption is transparent to Realm software, but has an impact on the security posture of a Realm.


## A11.1 Realm memory encryption overview

- A Memory Encryption Context (MEC) is an encryption regime used to protect the memory owned by a Realm.

The memory protected by a Realm's MEC includes all memory which can be accessed by the Realm, and the RTTs which are owned by the Realm.

Other Granules owned by the Realm, such as REC and RD, are protected with the RMM's MEC.

The number of MECs supported by an implementation is reported by the RMI\_FEATURES command in RmiFeatureRegister1::MEC\_COUNT.

If FEAT\_MEC is either not implemented or not enabled, MEC\_COUNT is zero.

On a platform which implements FEAT\_MEC, MEC\_COUNT is expected to be computed as follows:

- Determine the minimum MECID width supported across all system components capable of initiating Realm PAS transactions.
- Determine the number of MECIDs which the platform needs to reserve for its own use. This is expected to be at least one, for protection of the RMM's memory.
- Return MEC\_COUNT = (2 ^ MECID\_WIDTH)-(NUM\_RESERVED\_MECIDS + 1)

## See also:

- Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2]
- [A3.15 Support for Realm memory encryption](rmm-A3.md#a315-support-for-realm-memory-encryption)
- [B4.6.27 RmiFeatureRegister1 type](rmm-B4.6.md#b4627-rmifeatureregister1-type)

## A11.1.1 MEC and Realms

- RMI\_REALM\_CREATE fails if the system does not have an available MECID which satisfies the requested MEC policy.
- On a platform which reports MEC\_COUNT to be zero, all Realms use a Shared MEC.
- On a platform which reports MEC\_COUNT to be non-zero, the Host can choose between the following approaches:
- Use the Shared MEC for all Realms.
- Assign a Private MEC to each Realm, with the total number of Realms not exceeding MEC\_COUNT.


- Use the Shared MEC for some Realms; for the remaining Realms, assign a Private MEC to each, with the total number of this latter set of Realms not exceeding MEC\_COUNT.
- The Realm attestation token includes a claim which describes the MEC policy of the Realm.

## See also:

- [A7.2.3.1.8 Realm MEC policy claim](rmm-A7.2.3.1.md#a72318-realm-mec-policy-claim)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)

## A11.1.2 MEC and CMEM devices

- D0069 During Realm destruction, it may be necessary for the platform to perform MEC-related maintenance on CMEM devices. For example, if the Realm used a private MEC then before the corresponding CKID can be assigned to another Realm, its associated key must be regenerated. This maintenance is called PDEV MEC refresh .
- I0070 A PDEV MEC refresh is initiated by execution of RMI\_PDEV\_MEC\_REFRESH and is completed when the state of the PDEV transitions to PDEV\_READY.
- I0071 An input value of RMI\_PDEV\_MEC\_REFRESH identifies a Realm which is in REALM\_ZOMBIE state.
- R0072 When a Realm is in REALM\_ZOMBIE state, if a PDEV MEC refresh has not been completed on every PDEV for which all of the following are true then RMI\_REALM\_DESTROY fails:

- The PDEV is a member of a CMEM Interleave Set.
- Per-Realm encryption is enabled on the CMEM Interleave Set.

I0073 The following pseudocode illustrate the programming model for destroying a Realm, on a platform with CMEM devices.

```
// Destroy the Realm whose RD is located at rd_addr. // This function assumes that the Realm has already been made non-live. // // The pdev_addrs array contains the addresses of all CMEM PDEV objects. // // Checking of RmiResult returned by most commands is omitted // for brevity. int destroy_realm(uint64_t rd_addr, uint64_t *pdev_addrs, unsigned num_pdevs) { RmiResult result; uint64_t handle; // Move Realm into zombie state result = RMI_REALM_TERMINATE(rd_addr); for (unsigned i=0; i<num_pdevs; ++i) { uint64_t pdev = pdev_addrs[i]; struct RmiDevCommData data; // Initiate PDEV MEC refresh result = RMI_PDEV_MEC_REFRESH(pdev, rd); // Complete PDEV MEC refresh // Note that the first RMI_PDEV_COMMUNICATE is permitted // to return with no flags set, indicating that no // maintenance is required for this device. result = RMI_PDEV_COMMUNICATE(pdev, &data); while (data.flags) { if (data.exit.flags.req_send) { // Send request to device, wait for response, // and copy response into data.entry.resp_buf } result = RMI_PDEV_COMMUNICATE(pdev, &data); } } // Complete Realm destruction do { result = RMI_REALM_DESTROY(rd); } while (result.status == RMI_BUSY); while (result.status == RMI_BUSY || result.status == RMI_INCOMPLETE) { result = RMI_OP_CONTINUE(handle, flags=RMI_CONTINUE_KEEP_GOING); } return (int)result; }
```

See also:

- [A9.5 Communication between RMM and a device](rmm-A9.5.md)
- [A9.11 Coherent memory devices](rmm-A9.11.md)
- [B3.24 CmemMecUpdateComplete function](rmm-B3.md#b324-cmemmecupdatecomplete-function)
- [B4.5.30 RMI\_PDEV\_MEC\_REFRESH command](rmm-B4.5.30.md)
- [B4.5.47 RMI\_REALM\_DESTROY command](rmm-B4.5.47.md)

<!-- image -->

## Part B Interface