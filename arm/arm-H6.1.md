## H6.1 About Debug over powerdown

Arm A-profile external debug defines a logical model for the hardware on which a PE executes. This hardware is logically split into the Core power domain and the Debug power domain , and the model contains descriptions of the states of those domains. See:

- Power domains and debug.
- Core power domain power states.

An implementation may allow power domains to be powered up and down independently. Debug over powerdown provides:

- Afacility for software executing on the PE to save and restore the PE state on behalf of a self-hosted or external debugger or both. See Debug OS Save and Restore sequences.
- Afacility for an external debugger to request power up of the Core power domain. See Powerup request mechanism.
- Afacility for an external debugger, or software executing on the PE, to request emulation of powerdown of the Core power domain. See Emulating low-power states.