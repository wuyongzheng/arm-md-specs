## A9.6 Realm management of an assigned virtual device

This section describes interaction between a Realm and the RMM to manage an assigned virtual device.

- The Realm discovers an assigned PCIe TDI by probing PCIe config space. Arm expects that this will be emulated by the Host, via Unprotected IPA space.

See also:

- A9.4 Virtual device object

## A9.6.1 Realm retrieval of device attestation evidence

- A Realm is expected to retrieve cached device attestation evidence from the Host via an RSI\_HOST\_CALL interface. For details, refer to Realm Host Interface specification [20].
- A Realm can retrieve digests of the most recent device attestation evidence received by the RMM, by executing the RSI\_VDEV\_GET\_INFO command.

See also:

- A9.5.4 Host caching of device attestation evidence
- B5.4.5 RSI\_HOST\_CALL command
- B5.4.19 RSI\_VDEV\_GET\_INFO command

## A9.6.2 Realm validation of device memory mappings

- A Realm device interface report describes the memory regions of the device. Each device memory region has the following attributes in the report:
- PA base address of the region.

This is obfuscated by addition of a MMIO Reporting Offset (MRO) value to the system physical address. The offset value is known to the RMM.

- Size of the region.
- Whether the output address of the mapping is within the system coherent memory space.


Note that this is reported via an Arm-specific mechanism, described in RME system architecture spec [15].

- A Realm can validate by execution of RSI\_VDEV\_VALIDATE\_MAPPING that each MMIO region with IS\_NON\_TEE\_MEM=0 in the Realm device interface report has been correctly mapped into the Realm's Protected IPA space.
- In order to determine the IPA to pass into RSI\_VDEV\_VALIDATE\_MAPPING, the Realm uses the contents of the device interface report to calculate an offset which it adds to the virtual BAR address.

The ranges described in the device interface report may not cover the entire BAR. This can be due to the presence of region within the BAR which is TEE=0, and is therefore omitted from the device interface report.

Consequently, in order to calculate the virtual BAR offset, the Realm applies the following algorithm:

- Let (bar\_base, bar\_size) be the IPA range spanned by the virtual BAR. bar\_size is guaranteed by PCIe to be a power of two.
- Let (region\_base, region\_size) be an entry read from the device interface report. The device generated these pseudo-PA values by adding the MRO to the corresponding system physical address.
- Use the BAR size as an input to a modulus operation to calculate the offset of the region within the virtual BAR: region\_offset = region\_base % bar\_size

This algorithm assumes that the MRO value is a multiple of the BAR size.

- Arm recommends that the RMM should compute the MMIO Reporting Offset for a given VDEV using the following formula: MRO = x * 2^n

Where:

- x is a pseudo-random number.
- 2^n is guaranteed to be greater than or equal to the maximum BAR size for this VDEV.

Possible strategies for choosing 2^n include the following:

- Query PCIe configuration space to determine the maximum BAR size for this VDEV.
- Compute the maximum size among the device non-coherent address ranges (ncoh\_addr\_range) and device coherent address ranges (coh\_addr\_range) of the parent PDEV.
- Use the size of the platform's MMIO region.
- The input values of RSI\_VDEV\_VALIDATE\_MAPPING include the lock nonce, measurement sequence and report sequence values retrieved from the earlier call to RSI\_VDEV\_GET\_INFO. These are used to ensure that the configuration of the device has not changed between verification of device attestation evidence, and validation of device memory mappings.
- PCIe classifies memory locations into the following categories:
- 'TEE memory': must have mechanisms to ensure confidentiality of data. May additionally provide integrity properties on the data. In a CCA system, this category corresponds to memory locations within Realm PAS.
- · 'Non-TEE memory': assumed not to have mechanisms to ensure confidentiality or integrity of data. In a CCA system, this category corresponds to memory locations in Non-Secure PAS. IXSKML Arm recommends that RSI\_VDEV\_VALIDATE\_MAPPING is only called for TEE memory device locations. The RMM does not prevent validation of mappings to Non-TEE memory device locations. However, because all accesses to device memory via Protected IPA space are made with the IDE T-bit set to 1, access to a Non-TEE memory location may be rejected by the device. For further details, refer to PCI Express 6.0 specification [16]. IMGCSD Execution of RSI\_VDEV\_VALIDATE\_MAPPING initiates a VDEV mapping validation request. On execution of RSI\_VDEV\_VALIDATE\_MAPPING, the RMM records the PA base address of the region and the flags provided by the Realm in the REC. On subsequent execution of RMI\_RTT\_DEV\_VALIDATE, the RMM validates that the contents of the target RTTE are compatible with the PA base address of the region and the flags provided by the Realm. If this validation passes then the RMM sets the RIPAS of the RTTE to RIPAS\_DEV.
- The RTTE attributes checked by RMI\_RTT\_DEV\_VALIDATE, when the target RIPAS is RIPAS\_DEV, are as follows:
- The IPA to PA mapping is consistent with the PA base address of the region provided by the Realm.
- The RIPAS of the target region of IPA space is RIPAS\_EMPTY.
- The memory attributes are consistent with the value of the 'coh' flag provided by the Realm.
- -If coh == RSI\_DEV\_MEM\_COHERENT then expected memory attributes are MEMATTR\_PASSTHROUGH.
- -If coh == RSI\_DEV\_MEM\_NON\_COHERENT then expected memory attributes are MEMATTR\_NON\_CACHEABLE.
- The PA is within a PDEV address range which is consistent with the 'coh' flag provided by the Realm.
- -If coh == RSI\_DEV\_MEM\_COHERENT then the PA is expected to be within pdev.coh\_addr\_range.
- -If coh == RSI\_DEV\_MEM\_NON\_COHERENT then the PA is expected to be within pdev.ncoh\_addr\_range.
- The limited ordering properties of the PA (LOR or non-LOR) are consistent with the 'order' flag provided by the Realm.

## Chapter A9. Realm device assignment

## A9.6. Realm management of an assigned virtual device


Creation and validation of device memory mappings is illustrated in the following sequence diagram.

Figure A9.16: Creation and validation of device memory mappings

<!-- image -->

See also:

- PCI Express 6.0 specification [16]
- A5.5 VDEV mapping validation
- A5.6.12 Memory attributes
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command


## A9.6.3 Realm enablement of device DMA

- A Realm can enable device DMA by calling RSI\_VDEV\_DMA\_ENABLE.
- The input values of RSI\_VDEV\_DMA\_ENABLE include the lock nonce, measurement sequence and report sequence values retrieved from the earlier call to RSI\_VDEV\_GET\_INFO. These are used to ensure that the configuration of the device has not changed between verification of device attestation evidence, and enablement of device DMA.
- RSI\_VDEV\_DMA\_ENABLE fails unless the state of the VDEV is VDEV\_STARTED.

See also:

- B5.4.18 RSI\_VDEV\_DMA\_ENABLE command

<!-- image -->