## 2.1 History

- SMMUv1 supports a modest number of contexts/streams configured using registers, limiting scalability.
- SMMUv2 extends SMMUv1 with Armv8-A translation table formats, large addresses, with the same limited number of contexts and streams.

SMMUv1 and SMMUv2 map an incoming data stream onto one of many register-based context banks which indicate translation tables and translation configuration to use. The context bank might also indicate a second context bank for nested translation of a second stage (stage 1 and stage 2). The stream is identified using an externally-generated ID supplied with each transaction. A second ID might be supplied to determine the Security state of a stream or group of streams. The use of register-based configuration limits the number of context banks and support of thousands of concurrent contexts is not possible.

Because live data streams might potentially present transactions at any time, the available number of contexts limits the number of streams that might be concurrently enabled. For example, a system might have 1000 network interfaces that might all be idle but whose DMA might be triggered by incoming traffic at any time. The streams must be constantly available to function correctly. It is usually not possible to time-division multiplex a context between many devices requiring service.

The SMMU programming interface register SMMU\_AIDR indicates which SMMU architecture version the SMMUimplements, as follows:

- If SMMU\_AIDR[7:0] == 0x00 , the SMMU implements SMMUv3.0. · If SMMU\_AIDR[7:0] == 0x01 , the SMMU implements SMMUv3.1. · If SMMU\_AIDR[7:0] == 0x02 , the SMMU implements SMMUv3.2. · If SMMU\_AIDR[7:0] == 0x03 , the SMMU implements SMMUv3.3. · If SMMU\_AIDR[7:0] == 0x04 , the SMMU implements SMMUv3.4.

Unless specified otherwise, all architecture behaviors apply equally to all minor revisions of SMMUv3.