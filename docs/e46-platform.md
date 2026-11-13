# E46 platform overview

The **E46** is the fourth-generation BMW 3 Series (model years roughly **1999–2006** in most markets; pre-facelift vs facelift matters for lights, interior, and some electronics).

## Body styles

| Style | Notes |
|-------|--------|
| Sedan | Most common; good swap candidate |
| Touring (wagon) | Same floorpan concerns as sedan; rear weight bias |
| Coupe | Longer doors; similar engine bay to sedan |
| Convertible | **Heavier**, extra bracing; structural considerations for power increases |
| M3 (E46) | S54 from factory; unique subframe/suspension/brakes in many regions |

## Drivetrain layout

- **Longitudinal** engine, **RWD** (most E46s). **xi** models are AWD (transfer case, front driveshaft — swaps are harder).
- Manual: typically **Getrag 6-speed** (e.g. GS6-37BZ on many 6-cyl cars) or 5-speed on some 4-cyl.
- Auto: GM-based automatics (e.g. 5HP19 on many 6-cyl); swapping to manual is a separate project (pedals, wiring, DME, driveshaft, shifter).

## Generations (facelift)

- **Pre-LCI** (~1999–2001): early iDrive-less interiors; different headlight/taillight shapes.
- **LCI** (~2002–2006): facelift exterior; incremental electronics updates.

For swaps, the important splits are often **engine family already in the car**, **DME generation**, **OBD requirements**, and **whether you keep BMW CAN/bus modules happy**.

## Subframes & engine mounts

- Six-cylinder cars use the **M52/M54** style mounting pattern in the bay.
- **S50/S52/S54** (M cars) and **M54** share familial relationships but mounts, oil pan clearance, headers, and ECU differ.
- Non-BMW swaps (LS, 2JZ, etc.) usually need **aftermarket mounts**, **custom headers**, and often **steering rack / subframe** clearance work.

## Electronics (high level)

- **DME** (engine ECU), **EWS** (immobilizer), **instrument cluster**, **ASC/DSC**, **IHKA** (climate), and various **CAN** modules expect coherent messages.
- “Drop in” BMW engine swaps often mean: **matching or flashed DME**, **correct wiring harness** (or merged harness), **EWS sync**, and **cluster coding** for displacement/errors.
- Standalone ECUs (Megasquirt, Emtron, etc.) simplify engine control but increase integration work for gauges, AC, and inspections.

## What to document for *your* car

- VIN decode (market, year, factory engine code)
- Build date (facelift and option packages)
- OBD generation and emissions equipment (cats, SAP, secondary air, EVAP)
- Current transmission type and final drive ratio
- Existing options (sport package, LSD, xi vs RWD)

See [stock-engines.md](stock-engines.md) and [swap-work-areas.md](swap-work-areas.md).
