# ANSIS Soil Domain Enumerations
**JSON Schema Location:** enum.json

ANSIS controlled vocabularies converted to JSON schema enumerations. Follow the link under the vocabulary's title for full definitions.

> Enumerations defined according to the pattern recommended here: https://github.com/json-schema-org/json-schema-spec/issues/57

## ANSIS Core Entity Types

**ANSIS Vocabulary Location:** https://anzsoil.org/def/au/domain

Core ANSIS entities (features) served by the ANSIS system.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ansis:LandSurveySite | Land Survey Site |
| ansis:SoilBody | Soil Body |
| ansis:SoilHorizon | Soil Horizon |
| ansis:SoilLayer | Soil Layer |
| ansis:SoilProfile | Soil Profile |
| ansis:Soilample | Soil Sample |
| ansis:SoilSite | Soil Site |
| ansis:SoilSurface | Soil Surface |
| ansis:Substrate | Substrate |
| ansis:Treatment | Treatment |


## ANSIS Sampled Entity Types

**ANSIS Vocabulary Location:** https://anzsoil.org/def/au/domain

ANSIS entities that may be sampled (the component of a sample).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ansis:SoilBody | Soil Body |
| ansis:SoilHorizon | Soil Horizon |
| ansis:SoilLayer | Soil Layer |
| ansis:SoilSurface | Soil Surface |
| ansis:Substrate | Substrate |
| ansis:CoarseFragments | ANSIS Coarse Fragments |
| ansis:Cracks | ANSIS Cracks |
| ansis:Cutans | ANSIS Cutans |
| ansis:Landform | ANSIS Landform |
| ansis:Mottles | ANSIS Mottles |
| ansis:Outcrop | ANSIS Outcrop |
| ansis:Pans | ANSIS Pans |
| ansis:Pores | ANSIS Pores |
| ansis:Roots | ANSIS Roots |
| ansis:Segregations | ANSIS Segregations |
| ansis:SoilStructure | ANSIS Soil Structure |
| ansis:StreamChannel | ANSIS Stream Channel |


## Aggradation

**ANSIS Vocabulary Location:** ls:Aggradation

This refers to the presence of material deposited on a pre-existing surface as a result of wind and/or water erosion.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:aggradation-0 | No aggradation |
| ls:aggradation-1 | Present |
| ls:aggradation-X | Not apparent |


## Structure of artificial aggregates

**ANSIS Vocabulary Location:** sp:Artificial-aggregates-structure

Cultivated horizons (Ap horizons) often consist of artificial aggregates formed by cultivation or work being done on the soil. The distinction between artificial aggregates and peds can be difficult. In cultivated horizons, where the pedologist is confident the aggregates are natural peds they should be recorded as such. If the pedologist is doubtful, or the aggregates are obviously artificial, they should be recorded as clods or fragments.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:structure-artificial-CL | Clod |
| sp:structure-artificial-FR | Fragment |


## ASC Classifier - code

**ANSIS Vocabulary Location:** asc:Classifier-code

Australian Soil Classification Classifier - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## ASC Depth - code

**ANSIS Vocabulary Location:** asc:Depth-code

Australian Soil Classification Depth - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## ASC Gravel - code

**ANSIS Vocabulary Location:** asc:Gravel-code

Australian Soil Classification Gravel - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## ASC Order - code

**ANSIS Vocabulary Location:** asc:Order-code

Australian Soil Classification Order - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## ASC Texture - code

**ANSIS Vocabulary Location:** asc:Texture-code

Australian Soil Classification Texture - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## ASC Thickness - code

**ANSIS Vocabulary Location:** asc:Thickness-code

Australian Soil Classification Thickness - code.

> ASC ontology/vocabulary is not yet complete. https://github.com/ANZSoilData/def-au-asc/tree/master

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## Boundary distinctness

**ANSIS Vocabulary Location:** sp:Boundary-distinctness

Distinctness of the boundaries between horizons

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:horizon-boundary-distinctness-A | Abrupt |
| sp:horizon-boundary-distinctness-C | Clear (horizon boundary distinctness) |
| sp:horizon-boundary-distinctness-D | Diffuse (horizon boundary distinctness) |
| sp:horizon-boundary-distinctness-G | Gradual (horizon boundary distinctness) |
| sp:horizon-boundary-distinctness-S | Sharp (horizon boundary distinctness) |


## Boundary shape

**ANSIS Vocabulary Location:** sp:Boundary-shape

Shape of boundary between horizons

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:horizon-boundary-shape-B | Broken (horizon boundary shape) |
| sp:horizon-boundary-shape-I | Irregular |
| sp:horizon-boundary-shape-S | Smooth |
| sp:horizon-boundary-shape-T | Tongued |
| sp:horizon-boundary-shape-W | Wavy |


## Effervescence of carbonate in fine earth

**ANSIS Vocabulary Location:** sp:Carbonate-effervescence

Effervescence of carbonate in fine earth using two or three drops of 1-molar HCl.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:effervescence-H | Highly calcareous |
| sp:effervescence-M | Moderately calcareous |
| sp:effervescence-N | Non-calcareous |
| sp:effervescence-S | Slightly calcareous |
| sp:effervescence-V | Very highly calcareous |


## Stream channel depth relative to width

**ANSIS Vocabulary Location:** lf:Channel-depth-width

Channel depth and width refer to the dimensions of a landform that is dominated by channelled stream flow. The limit of channelled stream flow dominance must be identified before width or depth can be estimated. Depth is taken from the top of the stream bank down to the average height of the line following the deepest part of the channel.
The distinction between stream bank and hillslope or scarp according to dominant process requires particular care where streams are incised, especially if they are cut into terraces that could be mistaken for flood plains.
 
For detailed studies, keep records of width and depth measurements. In other surveys, use the following classes of relative depth.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-relative-depth-width-D | Deep |
| lf:stream-channel-relative-depth-width-M | Moderately deep |
| lf:stream-channel-relative-depth-width-S | Shallow |
| lf:stream-channel-relative-depth-width-V | Very shallow |


## Stream channel development

**ANSIS Vocabulary Location:** lf:Channel-development

The degree of development of stream channels.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-development-A | Alluvial |
| lf:stream-channel-development-E | Erosional |
| lf:stream-channel-development-I | Incipient |
| lf:stream-channel-development-O | Absent |


## Stream channel network directionality

**ANSIS Vocabulary Location:** lf:Channel-directionality

This attribute combines two simpler attributes: the degree of lineation, that is, the degree to which the channels tend to align in an organised way; and the degree of convergence or divergence of channels in the downstream direction. The latter is distinct from tributary/distributary behaviour, which refers to the combining and splitting of stream channels, rather than their directionality.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-network-directionality-B | Bidirectional |
| lf:stream-channel-network-directionality-C | Convergent |
| lf:stream-channel-network-directionality-D | Divergent |
| lf:stream-channel-network-directionality-F | Centrifugal |
| lf:stream-channel-network-directionality-N | Non-directional |
| lf:stream-channel-network-directionality-P | Centripetal |
| lf:stream-channel-network-directionality-U | Unidirectional |


## Stream channel network integration

**ANSIS Vocabulary Location:** lf:Channel-integration

In an integrated channel network, one can traverse from any point on a stream channel to any other point on a stream channel without passing through any landform elements other than stream channels. The channel network may be interrupted at points where water loss into the ground or the atmosphere is sufficiently large, and in the extreme case, typical of karst terrain, the surface stream network is disintegrated. Classes of channel network integration are:

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-network-integration-D | Disintegrated |
| lf:stream-channel-network-integration-I | Integrated |
| lf:stream-channel-network-integration-P | Interrupted (partial integration) |


## Stream channel migration

**ANSIS Vocabulary Location:** lf:Channel-migration

The presence of relict channel landforms or unvegetated, newly formed channel margins or immovable channel margins may permit an assessment of channel migration.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-migration-F | Fixed |
| lf:stream-channel-migration-R | Rapidly migrating |
| lf:stream-channel-migration-S | Slowly migrating |


## Stream-wise channel pattern

**ANSIS Vocabulary Location:** lf:Channel-pattern

In a traverse downstream, it may happen that tributaries enter the stream at frequent intervals, or that the stream splits into distributaries, or that these tendencies are absent (the non-tributary case) or are in balance with each other (the braided or anastomotic case called here reticulated) giving four classes of stream-wise channel pattern.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:streamwise-channel-pattern-D | Distributary |
| lf:streamwise-channel-pattern-N | Non-tributary |
| lf:streamwise-channel-pattern-R | Reticulated |
| lf:streamwise-channel-pattern-T | Tributary |


## Stream channel spacing

**ANSIS Vocabulary Location:** lf:Channel-spacing

The average spacing of stream channels, L/N, is determined by counting the number, N, of their intersections with an arbitrary line of length L.*
A convenient tool for estimating channel spacing is a circle, with a circumference of 2 km at map or photo scale, drawn on transparent material.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:stream-channel-spacing-AB | Absent or very rare |
| lf:stream-channel-spacing-CS | Closely spaced |
| lf:stream-channel-spacing-MS | Moderately spaced |
| lf:stream-channel-spacing-NU | Numerous |
| lf:stream-channel-spacing-SP | Sparse |
| lf:stream-channel-spacing-VC | Very closely spaced |
| lf:stream-channel-spacing-VW | Very widely spaced |
| lf:stream-channel-spacing-WS | Widely spaced |


## Abundance of coarse fragments

**ANSIS Vocabulary Location:** ls:Coarse-fragments-abundance

The percentage of coarse fragments.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:coarse-fragments-abundance-0 | No coarse fragments |
| ls:coarse-fragments-abundance-1 | Very slightly or very few |
| ls:coarse-fragments-abundance-2 | Slightly or few |
| ls:coarse-fragments-abundance-3 | No qualifier or common |
| ls:coarse-fragments-abundance-4 | Moderately or many |
| ls:coarse-fragments-abundance-5 | Very or abundant |
| ls:coarse-fragments-abundance-6 | Extremely or very abundant |


## Distribution of coarse fragments

**ANSIS Vocabulary Location:** sp:Coarse-fragments-distribution

Coarse fragments may occur throughout the profile.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:coarse-fragments-distribution-D | Dispersed |
| sp:coarse-fragments-distribution-R | Reoriented |
| sp:coarse-fragments-distribution-S | Stratified |
| sp:coarse-fragments-distribution-U | Undisturbed |


## Shape of coarse fragments

**ANSIS Vocabulary Location:** ls:Coarse-fragments-shape

The shape of coarse fragments is determined by referencing the chart that captures the roundness and sphericity. (Figure 12)

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:coarse-fragments-shape-A | Angular |
| ls:coarse-fragments-shape-AP | Angular platy |
| ls:coarse-fragments-shape-AT | Angular tabular |
| ls:coarse-fragments-shape-R | Rounded |
| ls:coarse-fragments-shape-RP | Rounded platy |
| ls:coarse-fragments-shape-RT | Rounded tabular |
| ls:coarse-fragments-shape-S | Subangular |
| ls:coarse-fragments-shape-SP | Subangular platy |
| ls:coarse-fragments-shape-ST | Subangular tabular |
| ls:coarse-fragments-shape-U | Subrounded |
| ls:coarse-fragments-shape-UP | Subrounded platy |
| ls:coarse-fragments-shape-UT | Subrounded tabular |


## Size of coarse fragments

**ANSIS Vocabulary Location:** ls:Coarse-fragments-size

The scale adopted employs class boundaries at (2 × 10n/2) mm, where n is an integer. This system is an extension of that used for particles smaller than 2 mm both in the scheme of the British Standards Institution and the Massachusetts Institute of Technology and the original Atterberg (1905) scheme on which the International Scheme was based. It is thus compatible with both the International Scheme referred to in the field texture section and the grain size criteria for substrate materials.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:coarse-fragments-size-1 | Fine gravelly or small pebbles |
| ls:coarse-fragments-size-2 | Medium gravelly or medium pebbles |
| ls:coarse-fragments-size-3 | Coarse gravelly or large pebbles |
| ls:coarse-fragments-size-4 | Cobbly or cobbles |
| ls:coarse-fragments-size-5 | Stony or stones |
| ls:coarse-fragments-size-6 | Bouldery or boulders |
| ls:coarse-fragments-size-7 | Large boulders |


## Moisture status for colour description

**ANSIS Vocabulary Location:** sp:Colour-moisture-status

Moisture status for colour description

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:colour-stat-D | Dry (colour status) |
| sp:colour-stat-M | Moist |


## Plasticity Degree

**ANSIS Vocabulary Location:** sp:Consistence-plasticity-degree

Plasticity is the ability to change shape and retain the new shape after the stress is removed. The degree of plasticity given below applies only to normal plasticity. The degree of plasticity is determined at the soil moisture content used for field texturing, that is, just below sticky point. The soil is rolled between the palms of the hand and, if possible, 40 mm long rolls are formed. The rolls are dangled from the thumb and forefinger. Plasticity is determined on the behaviour of rolls of varying thickness.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:consistence-plasticity-degree-0 | Non-plastic |
| sp:consistence-plasticity-degree-1 | Slightly plastic |
| sp:consistence-plasticity-degree-2 | Moderately plastic |
| sp:consistence-plasticity-degree-3 | Very plastic |


## Plasticity Type

**ANSIS Vocabulary Location:** sp:Consistence-plasticity-type

The type of plasticity refers to the degree to which either the consistence, field texture or both properties of a soil suggest the amount of clay-sized particles it contains (Butler 1955). It may be identified by determining two field textures: one after an initial 1 to 2 minute working of the soil sample, and another after a prolonged 10 minute kneading. The change in field texture from the initial to the prolonged working of the soil sample indicates the type of plasticity.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:consistence-plasticity-type-N | Normal plasticity |
| sp:consistence-plasticity-type-S | Superplastic |
| sp:consistence-plasticity-type-T | Strongly subplastic |
| sp:consistence-plasticity-type-U | Subplastic |


## Stickiness

**ANSIS Vocabulary Location:** sp:Consistence-stickiness

Stickiness is determined on wet soil by pressing the wet sample between thumb and forefinger and then observing the adherence of the soil to the fingers.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:consistence-stickiness-0 | Non-sticky |
| sp:consistence-stickiness-1 | Slightly sticky |
| sp:consistence-stickiness-2 | Moderately sticky |
| sp:consistence-stickiness-3 | Very sticky |


## Strength

**ANSIS Vocabulary Location:** sp:Consistence-strength

Strength of soil is the resistance to breaking or deformation. Strength is determined by the force just sufficient to break or deform a 20 mm diameter piece of soil when a compressive shearing force is applied between thumb and forefinger. The 20 mm piece of soil may be a ped, part of a ped, a compound ped or a fragment.

Forces 0 to 5 are equivalent to the following dry consistence classes in the ‘USDA Soil Survey Manual’ (Soil Survey Staff 1951):
0	Loose
1	Soft
2	Slightly hard
3	Hard
4	Very hard
5	Extremely hard

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:consistence-strength-0 | Loose (consistence strength) |
| sp:consistence-strength-1 | Very weak (consistence strength) |
| sp:consistence-strength-2 | Weak (consistence strength) |
| sp:consistence-strength-3 | Firm (consistence strength) |
| sp:consistence-strength-4 | Very Firm (consistence strength) |
| sp:consistence-strength-5 | Strong (consistence strength) |
| sp:consistence-strength-6 | Very Strong (consistence strength) |
| sp:consistence-strength-7 | Rigid (consistence strength) |


## Width of cracks

**ANSIS Vocabulary Location:** sp:Cracks-width

Width of planar voids

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:voids-cracks-1 | Fine (voids cracks) |
| sp:voids-cracks-2 | Medium (voids cracks) |
| sp:voids-cracks-3 | Coarse (voids cracks) |
| sp:voids-cracks-4 | Very coarse (voids cracks) |
| sp:voids-cracks-5 | Extremely coarse (voids cracks) |


## Abundance of cutans

**ANSIS Vocabulary Location:** sp:Cutans-abundance

Abundance of cutans

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:cutans-abundance-0 | No cutans |
| sp:cutans-abundance-1 | Few (cutans abundance) |
| sp:cutans-abundance-2 | Common (cutans abundance) |
| sp:cutans-abundance-3 | Many (cutans abundance) |


## Distinctness of cutans

**ANSIS Vocabulary Location:** sp:Cutans-distinctness

This refers to the ease and certainty with which a cutan is identified. Distinctness relates to thickness and to the colour contrast with the adjacent material; it may change markedly with moisture content.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:cutans-distinctness-D | Distinct (cutans distinctness) |
| sp:cutans-distinctness-F | Faint (cutans distinctness) |
| sp:cutans-distinctness-P | Prominent (cutans distinctness) |


## Types of cutans

**ANSIS Vocabulary Location:** sp:Cutans-type

Types of cutans

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:cutans-type-C | Clay skins |
| sp:cutans-type-K | Slickensides |
| sp:cutans-type-M | Mangans |
| sp:cutans-type-O | Other cutans |
| sp:cutans-type-S | Stress cutans |
| sp:cutans-type-U | Unspecified |
| sp:cutans-type-Z | Zero or no cutans |


## Disturbance of site

**ANSIS Vocabulary Location:** ls:Disturbance-of-site

These are broad categories of disturbance. Users may subdivide where considered necessary.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:disturbance-of-site-0 | No effective disturbance; natural |
| ls:disturbance-of-site-1 | No effective disturbance other than grazing by hoofed animals |
| ls:disturbance-of-site-2 | Limited clearing |
| ls:disturbance-of-site-3 | Extensive clearing |
| ls:disturbance-of-site-4 | Complete clearing; pasture, native or improved, but never cultivated |
| ls:disturbance-of-site-5 | Complete clearing; pasture, native or improved, cultivated at some stage |
| ls:disturbance-of-site-6 | Cultivation; rainfed |
| ls:disturbance-of-site-7 | Cultivation; irrigated, past or present |
| ls:disturbance-of-site-8 | Highly disturbed |


## Means of evaluation of elevation

**ANSIS Vocabulary Location:** ls:Elevation-evaluation-means

Means of evaluation of elevation

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:elevation-evaluation-means-A | Determined by altimeter |
| ls:elevation-evaluation-means-E | Estimate |
| ls:elevation-evaluation-means-L | Levelled from survey datum or estimated from contour plan |
| ls:elevation-evaluation-means-M | Interpolated from contour map |


## Gully depth

**ANSIS Vocabulary Location:** ls:Erosion-depth-gully

This gives the maximum depth within the site.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-G-depth-1 | Gully depth <1.5 m |
| ls:erosion-G-depth-2 | Gully depth 1.5-3.0 m |
| ls:erosion-G-depth-3 | Gully depth >3 m |


## Erosion severity

**ANSIS Vocabulary Location:** ls:Erosion-severity

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:Erosion-severity-gully | Gully erosion |
| ls:Erosion-severity-mass-movement | Mass movement |
| ls:Erosion-severity-rill | Rill erosion |
| ls:Erosion-severity-scald | Scald erosion |
| ls:Erosion-severity-sheet | Sheet erosion |
| ls:Erosion-severity-stream-bank | Stream bank erosion |
| ls:Erosion-severity-tunnel | Tunnel erosion |
| ls:Erosion-severity-wave | Wave erosion |
| ls:Erosion-severity-wind | Wind erosion |


## Gully erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-gully

A gully is a channel more than 0.3 m deep.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-G-0 | No gully erosion |
| ls:erosion-G-1 | Minor gully erosion |
| ls:erosion-G-2 | Moderate gully erosion |
| ls:erosion-G-3 | Severe gully erosion |


## Mass movement

**ANSIS Vocabulary Location:** ls:Erosion-severity-mass-movement

This includes all relatively large downslope movement of soil, rock or mixture of both, for example landslides, slumps, earth flows, debris avalanches and solifluxion.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-M-0 | No mass movement |
| ls:erosion-M-1 | Present |


## Rill erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-rill

A rill is a small channel up to 0.3 m deep, which can be largely obliterated by tillage operations (Houghton and Charman 1986).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-R-0 | No rill erosion |
| ls:erosion-R-1 | Minor |
| ls:erosion-R-2 | Moderate |
| ls:erosion-R-3 | Severe |


## Scald erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-scald

This is the removal of surface soil by water and/or wind, often exposing a more clayey subsoil which is devoid of vegetation and relatively impermeable to water. Scalds are most common in arid or semi-arid lands.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-C-0 | No scalding |
| ls:erosion-C-1 | Minor scalding |
| ls:erosion-C-2 | Moderate scalding |
| ls:erosion-C-3 | Severe scalding |


## Sheet erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-sheet

This is the relatively uniform removal of soil from an area without the development of conspicuous channels. Indicators of sheet erosion include soil deposits in downslope sediment traps, such as fencelines or farm dams, and pedestalling, root exposure or exposure of subsoils.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-S-0 | No sheet erosion |
| ls:erosion-S-1 | Minor |
| ls:erosion-S-2 | Moderate |
| ls:erosion-S-3 | Severe |
| ls:erosion-S-X | Not apparent |


## Stream bank erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-stream-bank

This is the removal of soil from a stream bank, typically during periods of high stream flow.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-B-0 | No stream bank erosion |
| ls:erosion-B-1 | Present |
| ls:erosion-B-X | Not apparent |


## Tunnel erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-tunnel

This is the removal of subsoil by water while the surface soil remains relatively intact (Crouch 1976).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-T-0 | No tunnel erosion |
| ls:erosion-T-1 | Present |
| ls:erosion-T-X | Not apparent |


## Wave erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-wave

Erosion of beaches, beach ridges and/or dunes. This is the removal of sand or soil from the margins of beaches, beach ridges, dunes, lakes or dams by wave action.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-V-0 | No wave erosion |
| ls:erosion-V-1 | Present |
| ls:erosion-V-X | Not apparent |


## Wind erosion

**ANSIS Vocabulary Location:** ls:Erosion-severity-wind

Give presence/absence or extent of accelerated erosion.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-W-0 | No wind erosion |
| ls:erosion-W-1 | Minor or present |
| ls:erosion-W-2 | Moderate |
| ls:erosion-W-3 | Severe |
| ls:erosion-W-4 | Very severe |
| ls:erosion-W-X | Not apparent |


## State of erosion

**ANSIS Vocabulary Location:** ls:Erosion-state

State of erosion

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-state-A | Active |
| ls:erosion-state-P | Partly stabilised |
| ls:erosion-state-S | Stabilised |


## Type of erosion

**ANSIS Vocabulary Location:** ls:Erosion-type

Type of erosion

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:erosion-type-B | Stream bank |
| ls:erosion-type-C | Scald |
| ls:erosion-type-G | Gully |
| ls:erosion-type-M | Mass movement |
| ls:erosion-type-R | Rill |
| ls:erosion-type-S | Sheet |
| ls:erosion-type-T | Tunnel |
| ls:erosion-type-V | Wave |
| ls:erosion-type-W | Wind |


## Fabric

**ANSIS Vocabulary Location:** sp:Fabric-type

The definition of soil fabric in Australia is incomplete. The following description is adapted from Northcote (1979).
Fabric describes the appearance of the soil material (under ×10 hand lens). Differences in fabric are associated with the presence or absence of peds, the lustre or lack of lustre of the ped surfaces, and the presence, size and arrangement of pores (voids) in the soil mass. The descriptions given below apply primarily to B horizons.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:fabric-E | Earthy (fabric) |
| sp:fabric-G | Sandy (grains prominent) |
| sp:fabric-R | Rough-ped |
| sp:fabric-S | Smooth-ped |


## Texture

**ANSIS Vocabulary Location:** subst:Field-texture

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:texture-A | Amorphous |
| subst:texture-F | Fragmental |
| subst:texture-P | Porphyritic |
| subst:texture-X | Crystalline (non-porphyritic) |


## Mineral soils field texture grade

**ANSIS Vocabulary Location:** sp:Field-texture-mineral

The following description of determination of field texture is adapted from Northcote (1979).
Field texture is a measure of the behaviour of a small handful of soil when moistened and kneaded into a ball and then pressed out between thumb and forefinger.
Take a sample of soil sufficient to fit comfortably into the palm of the hand. Moisten the soil with water, a little at a time, and knead until the ball of soil, so formed, just fails to stick to the fingers. Add more soil or water to attain this condition, known as the sticky point, which approximates field capacity for that soil. Continue kneading and moistening until there is no apparent change in the soil ball, usually a working time of 1–2 minutes. The soil ball, or bolus, is now ready for shearing manipulation, but the behaviour of the soil during bolus formation is also indicative of its field texture. The behaviour of the bolus and of the ribbon produced by shearing (pressing out) between thumb and forefinger characterises the field texture. Do not assess field texture grade solely on the length of ribbon.
The recommended field texture grades as characterised by the behaviour of the moist bolus are described. The approximate percentage content of clay (particles less than 0.002 mm in diameter) and silt (particles between 0.02 and 0.002 mm in diameter) are given as a guide. These percentages must not be used to determine a field texture, that is, do not use them to convert a laboratory particle size value to a field texture grade. Similarly, do not adjust a field texture grade when laboratory particle size data become available.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:field-texture-CL | Clay loam |
| sp:field-texture-CLS | Clay loam, sandy |
| sp:field-texture-CS | Clayey sand |
| sp:field-texture-HC | Heavy clay |
| sp:field-texture-L | Loam |
| sp:field-texture-LC | Light clay |
| sp:field-texture-LMC | Light medium clay |
| sp:field-texture-LS | Loamy sand |
| sp:field-texture-MC | Medium clay |
| sp:field-texture-MHC | Medium heavy clay |
| sp:field-texture-S | Sand (field texture) |
| sp:field-texture-SCL | Sandy clay loam |
| sp:field-texture-SL | Sandy loam |
| sp:field-texture-ZCL | Silty clay loam |
| sp:field-texture-ZL | Silty loam |


## Organic soils field texture

**ANSIS Vocabulary Location:** sp:Field-texture-organic

Organic soils do not have textural grades, as soil texture is determined by the size of mineral particles finer than 2 mm (NCST). In a sense, organic soils do have a texture related to the plant materials from which they formed and the degree of decomposition, exposure and drying. These field texture names may be used to characterise materials that on field examination are considered to be clearly dominated by organic matter. Peats may be assessed by examining the degree of decomposition and distinctness of plant remains. This work is adapted from Soil Survey Staff (1975) and Avery (1980).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:field-texture-AP | Sapric peat |
| sp:field-texture-CP | Clayey peat |
| sp:field-texture-GP | Granular peat |
| sp:field-texture-HP | Hemic peat |
| sp:field-texture-IP | Fibric peat |
| sp:field-texture-LP | Loamy peat |
| sp:field-texture-SP | Sandy peat |


## Geomorphological agents - biological agents

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-bio

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-BI | Non-human biological agents |
| lf:geomorphological-agent-HU | Human agents |


## Geomorphological agents - extraterrestrial agents

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-extra

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-IM | Impact by meteors |


## Geomorphological agents - gravity

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-gravity

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-GR | Gravity |


## Geomorphological agents - ice

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-ice

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-FR | Frost |
| lf:geomorphological-agent-GL | Glacier flow |


## Geomorphological agents - internal forces

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-internal

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-DI | Diastrophism |
| lf:geomorphological-agent-VO | Volcanism |


## Geomorphological agents - precipitation

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-precipitation

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-SH | Sheet flow, sheet wash, surface wash |
| lf:geomorphological-agent-SM | Soil moisture status changes |
| lf:geomorphological-agent-SO | Solution |
| lf:geomorphological-agent-WM | Water-aided mass movements |


## Geomorphological agents - standing water

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-stand

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-EU | Eustasy |
| lf:geomorphological-agent-TI | Tides |
| lf:geomorphological-agent-WA | Waves |


## Geomorphological agents - stream flow

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-streamflow

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-CH | Channelled stream flow |
| lf:geomorphological-agent-OV | Overbank stream flow, unchannelled |


## Geomorphological agents - wind

**ANSIS Vocabulary Location:** lf:Geomorphology-agent-wind

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:geomorphological-agent-WI | Wind |


## Mode of geomorphological activity

**ANSIS Vocabulary Location:** lf:Geomorphology-mode

Various modes of geomorphological activity may be distinguished (Figure 3).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:mode-of-geomorphological-activity-AG | Aggraded |
| lf:mode-of-geomorphological-activity-BU | Built up |
| lf:mode-of-geomorphological-activity-EA | Eroded or aggraded |
| lf:mode-of-geomorphological-activity-ER | Eroded |
| lf:mode-of-geomorphological-activity-EX | Excavated or dug out |
| lf:mode-of-geomorphological-activity-HU | Heaved up or elevated |
| lf:mode-of-geomorphological-activity-SU | Subsided or depressed |


## Status of geomorphological activity

**ANSIS Vocabulary Location:** lf:Geomorphology-status

Status of geomorphological activity

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:status-of-geomorphological-activity-B | Barely active |
| lf:status-of-geomorphological-activity-C | Continuously active |
| lf:status-of-geomorphological-activity-F | Frequently active |
| lf:status-of-geomorphological-activity-R | Relict |
| lf:status-of-geomorphological-activity-S | Seldom active |
| lf:status-of-geomorphological-activity-U | Unspecified |


## Type of soil horizon

**ANSIS Vocabulary Location:** sp:Horizon-code

A soil horizon is a layer of soil, approximately parallel to the land surface, with morphological properties different from layers below and/or above it. Tongues of material from one horizon may penetrate into adjacent horizons. Give horizon notation as described below.

As horizon notation is deduced from the profile description data (Northcote 1979) and in some instances laboratory data, record it after the profile is described. Horizons may be difficult to name, but should be named in the field. Opinions formed at the time of description are useful for later reference.

With regard to horizon notation, the long-established usage in horizon designation is adopted. Emphasis is on factual objective notation rather than assumed genesis, as genetic implications are often uncertain and difficult to establish. Thus the notation E indicating eluvial horizon (International Society of Soil Science 1967) has not been used, even though this has been adopted by a number of overseas organisations, for example Hodgson (1974), Soil Survey Staff (1990).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:horizons-A | A horizons |
| sp:horizons-B | B horizons |
| sp:horizons-C | C horizons |
| sp:horizons-D | D horizons |
| sp:horizons-O | O horizons |
| sp:horizons-P | P horizons |
| sp:horizons-R | R horizons |


## Horizon suffixes

**ANSIS Vocabulary Location:** sp:Horizon-suffix

The horizon's alphabetic suffix is used to further define the horizon. It always comes after the numeric subdivision except for suffix p, where the number always follows the letter (e.g. Ap2).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:horizon-suffix-b | Horizon suffix b |
| sp:horizon-suffix-c | Horizon suffix c |
| sp:horizon-suffix-d | Horizon suffix d |
| sp:horizon-suffix-e | Horizon suffix e |
| sp:horizon-suffix-f | Horizon suffix f |
| sp:horizon-suffix-g | Horizon suffix g |
| sp:horizon-suffix-h | Horizon suffix h |
| sp:horizon-suffix-j | Horizon suffix j |
| sp:horizon-suffix-k | Horizon suffix k |
| sp:horizon-suffix-m | Horizon suffix m |
| sp:horizon-suffix-p | Horizon suffix p |
| sp:horizon-suffix-q | Horizon suffix q |
| sp:horizon-suffix-r | Horizon suffix r |
| sp:horizon-suffix-s | Horizon suffix s |
| sp:horizon-suffix-t | Horizon suffix t |
| sp:horizon-suffix-w | Horizon suffix w |
| sp:horizon-suffix-x | Horizon suffix x |
| sp:horizon-suffix-y | Horizon suffix y |
| sp:horizon-suffix-z | Horizon suffix z |


## Depth of inundation (annual)

**ANSIS Vocabulary Location:** ls:Inundation-depth

Give likely maximum depth of water in an inundation event (mm). 

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:inundation-depth-1 | Inundation depth <50 mm |
| ls:inundation-depth-2 | Inundation depth 50-100 mm |
| ls:inundation-depth-3 | Inundation depth 100-300 mm |
| ls:inundation-depth-4 | Inundation depth 300-1000 mm |
| ls:inundation-depth-5 | Inundation depth >1000 mm |


## Duration (annual) of inundation

**ANSIS Vocabulary Location:** ls:Inundation-duration

Give likely duration of an inundation event.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:inundation-duration-1 | Less than 1 day |
| ls:inundation-duration-2 | Between 1 and 20 days |
| ls:inundation-duration-3 | Between 20 and 120 days |
| ls:inundation-duration-4 | More than 120 days |


## Frequency of inundation

**ANSIS Vocabulary Location:** ls:Inundation-frequency

Give long-term average of inundation. Among alluvial plains, flood plains typically fall in categories 4 and 3.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:inundation-frequency-0 | No inundation |
| ls:inundation-frequency-1 | Less than one occurrence per 100 years |
| ls:inundation-frequency-2 | One occurrence in between 50 and 100 years |
| ls:inundation-frequency-3 | One occurrence in between 10 and 50 years |
| ls:inundation-frequency-4 | One occurrence in between 1 and 10 years |
| ls:inundation-frequency-5 | More than one occurrence per year |


## Glossary of landform elements

**ANSIS Vocabulary Location:** lf:Landform-element-name

The landform element glossary aims to provide an adequate, concise set of names for types of landform element.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:landform-element-ALC | Alcove |
| lf:landform-element-BAN | Bank (stream bank) |
| lf:landform-element-BAR | Bar (stream bar) |
| lf:landform-element-BEA | Beach |
| lf:landform-element-BEN | Bench |
| lf:landform-element-BER | Berm |
| lf:landform-element-BKP | Backplain |
| lf:landform-element-BOU | Blow-out |
| lf:landform-element-BRI | Beach ridge |
| lf:landform-element-BRK | Breakaway |
| lf:landform-element-CBE | Channel bench |
| lf:landform-element-CFS | Cliff-footslope |
| lf:landform-element-CIR | Cirque |
| lf:landform-element-CLI | Cliff |
| lf:landform-element-CON | Cone (volcanic) |
| lf:landform-element-COS | Cut-over surface |
| lf:landform-element-CRA | Crater |
| lf:landform-element-CUT | Cut face |
| lf:landform-element-DAM | Dam |
| lf:landform-element-DBA | Deflation basin |
| lf:landform-element-DDE | Drainage depression |
| lf:landform-element-DOC | Collapse doline |
| lf:landform-element-DOL | Solution doline |
| lf:landform-element-DUB | Barchan dune |
| lf:landform-element-DUC | Dunecrest |
| lf:landform-element-DUF | Linear or longitudinal (seif) dune |
| lf:landform-element-DUH | Hummocky (weakly oriented) dune |
| lf:landform-element-DUN | Dune |
| lf:landform-element-DUP | Parabolic dune |
| lf:landform-element-DUS | Duneslope |
| lf:landform-element-EMB | Embankment |
| lf:landform-element-EST | Estuary |
| lf:landform-element-FAN | Fan |
| lf:landform-element-FIL | Fill-top |
| lf:landform-element-FLD | Flood-out |
| lf:landform-element-FOO | Footslope |
| lf:landform-element-FOR | Foredune |
| lf:landform-element-GUL | Gully |
| lf:landform-element-HCR | Hillcrest |
| lf:landform-element-HSL | Hillslope |
| lf:landform-element-ITF | Intertidal flat |
| lf:landform-element-LAG | Lagoon |
| lf:landform-element-LAK | Lake |
| lf:landform-element-LDS | Landslide |
| lf:landform-element-LEV | Levee |
| lf:landform-element-LUN | Lunette |
| lf:landform-element-MAA | Maar |
| lf:landform-element-MOU | Mound |
| lf:landform-element-OXB | Ox-bow |
| lf:landform-element-PED | Pediment |
| lf:landform-element-PIT | Pit |
| lf:landform-element-PLA | Plain |
| lf:landform-element-PLY | Playa |
| lf:landform-element-PST | Prior stream |
| lf:landform-element-REC | Risecrest |
| lf:landform-element-REF | Reef flat |
| lf:landform-element-RER | Residual rise |
| lf:landform-element-RES | Riseslope |
| lf:landform-element-RFL | Rock flat |
| lf:landform-element-RPL | Rock platform |
| lf:landform-element-SCA | Scarp |
| lf:landform-element-SCD | Scald |
| lf:landform-element-SCR | Scroll |
| lf:landform-element-SFS | Scarp-footslope |
| lf:landform-element-SRP | Scroll plain |
| lf:landform-element-STB | Stream bed |
| lf:landform-element-STC | Stream channel |
| lf:landform-element-STF | Supratidal flat |
| lf:landform-element-SUS | Summit surface |
| lf:landform-element-SWL | Swale |
| lf:landform-element-SWP | Swamp |
| lf:landform-element-TAL | Talus |
| lf:landform-element-TDC | Tidal creek |
| lf:landform-element-TDF | Tidal flat |
| lf:landform-element-TEF | Terrace flat |
| lf:landform-element-TEP | Terrace plain |
| lf:landform-element-TOR | Tor |
| lf:landform-element-TRE | Trench |
| lf:landform-element-TUM | Tumulus |
| lf:landform-element-VLF | Valley flat |


## Morphological type

**ANSIS Vocabulary Location:** lf:Landform-element-type

Landform elements fall into morphological types as sketched in Figure 1. Ten types are distinguished.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:Relative-inclination | Relative inclination of slope elements |
| lf:compound-morphological-types | Compound morphological types |
| lf:morphological-type-C | Crest |
| lf:morphological-type-D | Closed depression |
| lf:morphological-type-F | Flat |
| lf:morphological-type-H | Hillock |
| lf:morphological-type-L | Lower slope (requires inclination modifier) |
| lf:morphological-type-LA | Lower slope Maximal |
| lf:morphological-type-LI | Lower slope Minimal |
| lf:morphological-type-LN | Lower slope Waning |
| lf:morphological-type-LX | Lower slope Waxing |
| lf:morphological-type-M | Mid-slope (requires inclination modifier) |
| lf:morphological-type-MA | Mid-slope Maximal |
| lf:morphological-type-MI | Mid-slope Minimal |
| lf:morphological-type-MN | Mid-slope Waning |
| lf:morphological-type-MX | Mid-slope Waxing |
| lf:morphological-type-R | Ridge |
| lf:morphological-type-S | Simple slope |
| lf:morphological-type-U | Upper slope (requires inclination modifier) |
| lf:morphological-type-UA | Upper slope Maximal |
| lf:morphological-type-UI | Upper slope Minimal |
| lf:morphological-type-UN | Upper slope Waning |
| lf:morphological-type-UX | Upper slope Waxing |
| lf:morphological-type-V | Open depression (vale) |


## Simple erosional landform patterns

**ANSIS Vocabulary Location:** lf:Landform-pattern-erosional

Simple erosional landform patterns are based on relief and modal slope.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:simple-erosional-landform-pattern-B | Badlands (simple erosional pattern) |
| lf:simple-erosional-landform-pattern-GP | Gently undulating plain |
| lf:simple-erosional-landform-pattern-GR | Gently undulating rises |
| lf:simple-erosional-landform-pattern-LP | Level plain |
| lf:simple-erosional-landform-pattern-PH | Precipitous hills |
| lf:simple-erosional-landform-pattern-PM | Precipitous mountains |
| lf:simple-erosional-landform-pattern-RH | Rolling hills |
| lf:simple-erosional-landform-pattern-RL | Rolling low hills |
| lf:simple-erosional-landform-pattern-RM | Rolling mountains |
| lf:simple-erosional-landform-pattern-RP | Rolling plain |
| lf:simple-erosional-landform-pattern-RR | Rolling rises |
| lf:simple-erosional-landform-pattern-SH | Steep hills |
| lf:simple-erosional-landform-pattern-SL | Steep low hills |
| lf:simple-erosional-landform-pattern-SM | Steep mountains |
| lf:simple-erosional-landform-pattern-SR | Steep rises |
| lf:simple-erosional-landform-pattern-UH | Undulating hills |
| lf:simple-erosional-landform-pattern-UL | Undulating low hills |
| lf:simple-erosional-landform-pattern-UP | Undulating plain |
| lf:simple-erosional-landform-pattern-UR | Undulating rises |
| lf:simple-erosional-landform-pattern-VH | Very steep hills |
| lf:simple-erosional-landform-pattern-VL | Very steep low hills |
| lf:simple-erosional-landform-pattern-VM | Very steep mountains |


## Glossary of landform patterns

**ANSIS Vocabulary Location:** lf:Landform-pattern-name

The definitions in this glossary refer explicitly to the attributes of landform patterns that have been set down in the preceding sections.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:landform-pattern-ALF | Alluvial fan |
| lf:landform-pattern-ALP | Alluvial plain |
| lf:landform-pattern-ANA | Anastomotic plain |
| lf:landform-pattern-BAD | Badlands |
| lf:landform-pattern-BAR | Bar plain |
| lf:landform-pattern-BEA | Beach ridge plain |
| lf:landform-pattern-CAL | Caldera |
| lf:landform-pattern-CHE | Chenier plain |
| lf:landform-pattern-COR | Coral reef |
| lf:landform-pattern-COV | Covered plain |
| lf:landform-pattern-DEL | Delta |
| lf:landform-pattern-DUN | Dunefield |
| lf:landform-pattern-ESC | Escarpment |
| lf:landform-pattern-FLO | Food plain |
| lf:landform-pattern-HIL | Hills |
| lf:landform-pattern-KAR | Karst |
| lf:landform-pattern-LAC | Lacustrine plain |
| lf:landform-pattern-LAV | Lava plain |
| lf:landform-pattern-LON | Longitudinal dunefield |
| lf:landform-pattern-LOW | Low hills |
| lf:landform-pattern-MAD | Made land |
| lf:landform-pattern-MAR | Marine plain |
| lf:landform-pattern-MEA | Meander plain |
| lf:landform-pattern-MET | Meteor crater |
| lf:landform-pattern-MOU | Mountains |
| lf:landform-pattern-PAR | Parabolic dunefield |
| lf:landform-pattern-PED | Pediment (pattern) |
| lf:landform-pattern-PEP | Pediplain |
| lf:landform-pattern-PLA | Plain (pattern) |
| lf:landform-pattern-PLT | Plateau |
| lf:landform-pattern-PLY | Playa plain |
| lf:landform-pattern-PNP | Peneplain |
| lf:landform-pattern-RIS | Rises |
| lf:landform-pattern-SAN | Sand plain |
| lf:landform-pattern-SHF | Sheet-flood fan |
| lf:landform-pattern-STA | Stagnant alluvial plain |
| lf:landform-pattern-TEL | Terraced land (alluvial) |
| lf:landform-pattern-TER | Terrace (alluvial) |
| lf:landform-pattern-TID | Tidal flat (pattern) |
| lf:landform-pattern-VOL | Volcano |


## Lithology of coarse fragments

**ANSIS Vocabulary Location:** ls:Lithology-coarse-fragments

The lithology of the coarse fragments is usually identified as coming from the substrate or from rock outcrop. Where the lithology of the coarse fragments is different from that of the substrate material and/or rock outcrop, describe it as for lithology of substrate material only where the rock type is definitely known or is confidently presumed. Some coarse fragments are commonly encountered that are not directly related to the substrate material.    

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:lithology-CC | Charcoal |
| ls:lithology-IS | Ironstone |
| ls:lithology-M | Same as substrate material |
| ls:lithology-OT | Other |
| ls:lithology-OW | Opalised wood |
| ls:lithology-PU | Pumice |
| ls:lithology-R | Same as rock outcrop |
| ls:lithology-SS | Shells |


## Lithological type- rock

**ANSIS Vocabulary Location:** subst:Lithology-rock

Lithological type - rock.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:lithology-AC | Alcrete |
| subst:lithology-AD | Adamellite |
| subst:lithology-AF | Volcanic ash (fine) |
| subst:lithology-AG | Agglomerate |
| subst:lithology-AH | Anhydrite |
| subst:lithology-AM | Amphibolite |
| subst:lithology-AN | Andesite |
| subst:lithology-AP | Aplite |
| subst:lithology-AR | Arkose |
| subst:lithology-AS | Volcanic ash (sandy) |
| subst:lithology-BA | Basalt |
| subst:lithology-BB | Bombs (or blocks) |
| subst:lithology-BR | Breccia |
| subst:lithology-C | Clay |
| subst:lithology-CG | Conglomerate |
| subst:lithology-CH | Chert |
| subst:lithology-CO | Coal |
| subst:lithology-CU | Consolidated rock |
| subst:lithology-DI | Diorite |
| subst:lithology-DM | Dolomite |
| subst:lithology-DR | Dolerite |
| subst:lithology-FC | Ferricrete |
| subst:lithology-GA | Gabbro |
| subst:lithology-GD | Granodiorite |
| subst:lithology-GE | Greenstone |
| subst:lithology-GN | Granite |
| subst:lithology-GR | Granulite |
| subst:lithology-GS | Gneiss |
| subst:lithology-GV | Gravel |
| subst:lithology-GW | Graywacke |
| subst:lithology-GY | Gypsum |
| subst:lithology-HA | Halite |
| subst:lithology-HO | Hornfels |
| subst:lithology-IG | Igneous rock |
| subst:lithology-JA | Jasper |
| subst:lithology-KA | Calcarenite |
| subst:lithology-KC | Calcrete |
| subst:lithology-KL | Calcilutite |
| subst:lithology-KM | Calcareous mudstone |
| subst:lithology-KR | Calcirudite |
| subst:lithology-KS | Calcareous sand |
| subst:lithology-LC | Silcrete |
| subst:lithology-LI | Limestone |
| subst:lithology-M | Same as substrate material |
| subst:lithology-MB | Marble |
| subst:lithology-MD | Microdiorite |
| subst:lithology-ME | Metamorphic rock |
| subst:lithology-MG | Microgranite |
| subst:lithology-MI | Migmatite |
| subst:lithology-ML | Marl |
| subst:lithology-MS | Microsyenite |
| subst:lithology-MU | Mudstone |
| subst:lithology-MY | Mylonite |
| subst:lithology-PC | Porcellanite |
| subst:lithology-PE | Peridotite |
| subst:lithology-PG | Pegmatite |
| subst:lithology-PH | Phyllite |
| subst:lithology-PL | Phonolite |
| subst:lithology-PO | Porphyry |
| subst:lithology-PY | Pyroxenite |
| subst:lithology-QP | Quartz porphyry |
| subst:lithology-QS | Quartz sandstone |
| subst:lithology-QU | Quartzite |
| subst:lithology-QZ | Quartz |
| subst:lithology-R | Same as rock outcrop |
| subst:lithology-RB | Red-brown hardpan |
| subst:lithology-RH | Rhyolite |
| subst:lithology-S | Sand |
| subst:lithology-SA | Sandstone |
| subst:lithology-SD | Detrital sedimentary rock |
| subst:lithology-SH | Shale |
| subst:lithology-SK | Scoria |
| subst:lithology-SL | Slate |
| subst:lithology-SR | Serpentinite |
| subst:lithology-ST | Schist |
| subst:lithology-SY | Syenite |
| subst:lithology-TR | Trachyte |
| subst:lithology-TU | Tuff |
| subst:lithology-UC | Unconsolidated material |
| subst:lithology-VB | Volcanic breccia |
| subst:lithology-VG | Volcanic glass |
| subst:lithology-Z | Silt |
| subst:lithology-ZS | Siltstone |


## Lithology of rock outcrop

**ANSIS Vocabulary Location:** ls:Lithology-rock-outcrop

Where the lithology of the rock outcrop is different from that of the substrate material, record it as for lithology of substrate material. 

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| http://anzsoil.org/def/au/asls/substrate/lithology-AC | Alcrete |
| http://anzsoil.org/def/au/asls/substrate/lithology-AD | Adamellite |
| http://anzsoil.org/def/au/asls/substrate/lithology-AF | Volcanic ash (fine) |
| http://anzsoil.org/def/au/asls/substrate/lithology-AG | Agglomerate |
| http://anzsoil.org/def/au/asls/substrate/lithology-AH | Anhydrite |
| http://anzsoil.org/def/au/asls/substrate/lithology-AM | Amphibolite |
| http://anzsoil.org/def/au/asls/substrate/lithology-AN | Andesite |
| http://anzsoil.org/def/au/asls/substrate/lithology-AP | Aplite |
| http://anzsoil.org/def/au/asls/substrate/lithology-AR | Arkose |
| http://anzsoil.org/def/au/asls/substrate/lithology-AS | Volcanic ash (sandy) |
| http://anzsoil.org/def/au/asls/substrate/lithology-BA | Basalt |
| http://anzsoil.org/def/au/asls/substrate/lithology-BB | Bombs (or blocks) |
| http://anzsoil.org/def/au/asls/substrate/lithology-BR | Breccia |
| http://anzsoil.org/def/au/asls/substrate/lithology-C | Clay |
| http://anzsoil.org/def/au/asls/substrate/lithology-CG | Conglomerate |
| http://anzsoil.org/def/au/asls/substrate/lithology-CH | Chert |
| http://anzsoil.org/def/au/asls/substrate/lithology-CO | Coal |
| http://anzsoil.org/def/au/asls/substrate/lithology-CU | Consolidated rock |
| http://anzsoil.org/def/au/asls/substrate/lithology-DI | Diorite |
| http://anzsoil.org/def/au/asls/substrate/lithology-DM | Dolomite |
| http://anzsoil.org/def/au/asls/substrate/lithology-DR | Dolerite |
| http://anzsoil.org/def/au/asls/substrate/lithology-FC | Ferricrete |
| http://anzsoil.org/def/au/asls/substrate/lithology-GA | Gabbro |
| http://anzsoil.org/def/au/asls/substrate/lithology-GD | Granodiorite |
| http://anzsoil.org/def/au/asls/substrate/lithology-GE | Greenstone |
| http://anzsoil.org/def/au/asls/substrate/lithology-GN | Granite |
| http://anzsoil.org/def/au/asls/substrate/lithology-GR | Granulite |
| http://anzsoil.org/def/au/asls/substrate/lithology-GS | Gneiss |
| http://anzsoil.org/def/au/asls/substrate/lithology-GV | Gravel |
| http://anzsoil.org/def/au/asls/substrate/lithology-GW | Graywacke |
| http://anzsoil.org/def/au/asls/substrate/lithology-GY | Gypsum |
| http://anzsoil.org/def/au/asls/substrate/lithology-HA | Halite |
| http://anzsoil.org/def/au/asls/substrate/lithology-HO | Hornfels |
| http://anzsoil.org/def/au/asls/substrate/lithology-IG | Igneous rock |
| http://anzsoil.org/def/au/asls/substrate/lithology-JA | Jasper |
| http://anzsoil.org/def/au/asls/substrate/lithology-KA | Calcarenite |
| http://anzsoil.org/def/au/asls/substrate/lithology-KC | Calcrete |
| http://anzsoil.org/def/au/asls/substrate/lithology-KL | Calcilutite |
| http://anzsoil.org/def/au/asls/substrate/lithology-KM | Calcareous mudstone |
| http://anzsoil.org/def/au/asls/substrate/lithology-KR | Calcirudite |
| http://anzsoil.org/def/au/asls/substrate/lithology-KS | Calcareous sand |
| http://anzsoil.org/def/au/asls/substrate/lithology-LC | Silcrete |
| http://anzsoil.org/def/au/asls/substrate/lithology-LI | Limestone |
| http://anzsoil.org/def/au/asls/substrate/lithology-M | Same as substrate material |
| http://anzsoil.org/def/au/asls/substrate/lithology-MB | Marble |
| http://anzsoil.org/def/au/asls/substrate/lithology-MD | Microdiorite |
| http://anzsoil.org/def/au/asls/substrate/lithology-ME | Metamorphic rock |
| http://anzsoil.org/def/au/asls/substrate/lithology-MG | Microgranite |
| http://anzsoil.org/def/au/asls/substrate/lithology-MI | Migmatite |
| http://anzsoil.org/def/au/asls/substrate/lithology-ML | Marl |
| http://anzsoil.org/def/au/asls/substrate/lithology-MS | Microsyenite |
| http://anzsoil.org/def/au/asls/substrate/lithology-MU | Mudstone |
| http://anzsoil.org/def/au/asls/substrate/lithology-MY | Mylonite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PC | Porcellanite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PE | Peridotite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PG | Pegmatite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PH | Phyllite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PL | Phonolite |
| http://anzsoil.org/def/au/asls/substrate/lithology-PO | Porphyry |
| http://anzsoil.org/def/au/asls/substrate/lithology-PY | Pyroxenite |
| http://anzsoil.org/def/au/asls/substrate/lithology-QP | Quartz porphyry |
| http://anzsoil.org/def/au/asls/substrate/lithology-QS | Quartz sandstone |
| http://anzsoil.org/def/au/asls/substrate/lithology-QU | Quartzite |
| http://anzsoil.org/def/au/asls/substrate/lithology-QZ | Quartz |
| http://anzsoil.org/def/au/asls/substrate/lithology-R | Same as rock outcrop |
| http://anzsoil.org/def/au/asls/substrate/lithology-RB | Red-brown hardpan |
| http://anzsoil.org/def/au/asls/substrate/lithology-RH | Rhyolite |
| http://anzsoil.org/def/au/asls/substrate/lithology-S | Sand |
| http://anzsoil.org/def/au/asls/substrate/lithology-SA | Sandstone |
| http://anzsoil.org/def/au/asls/substrate/lithology-SD | Detrital sedimentary rock |
| http://anzsoil.org/def/au/asls/substrate/lithology-SH | Shale |
| http://anzsoil.org/def/au/asls/substrate/lithology-SK | Scoria |
| http://anzsoil.org/def/au/asls/substrate/lithology-SL | Slate |
| http://anzsoil.org/def/au/asls/substrate/lithology-SR | Serpentinite |
| http://anzsoil.org/def/au/asls/substrate/lithology-ST | Schist |
| http://anzsoil.org/def/au/asls/substrate/lithology-SY | Syenite |
| http://anzsoil.org/def/au/asls/substrate/lithology-TR | Trachyte |
| http://anzsoil.org/def/au/asls/substrate/lithology-TU | Tuff |
| http://anzsoil.org/def/au/asls/substrate/lithology-UC | Unconsolidated material |
| http://anzsoil.org/def/au/asls/substrate/lithology-VB | Volcanic breccia |
| http://anzsoil.org/def/au/asls/substrate/lithology-VG | Volcanic glass |
| http://anzsoil.org/def/au/asls/substrate/lithology-Z | Silt |
| http://anzsoil.org/def/au/asls/substrate/lithology-ZS | Siltstone |


## Lithological type- unconsolidated material

**ANSIS Vocabulary Location:** subst:Lithology-unconsolidated

Lithological type - unconsoldiated material.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:lithology-AF | Volcanic ash (fine) |
| subst:lithology-AS | Volcanic ash (sandy) |
| subst:lithology-BB | Bombs (or blocks) |
| subst:lithology-BO | Boulders |
| subst:lithology-C | Clay |
| subst:lithology-CB | Cobbles |
| subst:lithology-GV | Gravel |
| subst:lithology-KS | Calcareous sand |
| subst:lithology-ML | Marl |
| subst:lithology-S | Sand |
| subst:lithology-SK | Scoria |
| subst:lithology-SN | Stones |
| subst:lithology-Z | Silt |


## Location within the landform element

**ANSIS Vocabulary Location:** lf:Location-in-element

A site chosen to represent a landform element will often be placed centrally within it. For various reasons, a site may not be centrally placed and this should be recorded. The vertical position of the site within the height of the landform element may be the best measure:

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:location-within-the-landform-element-B | Bottom |
| lf:location-within-the-landform-element-M | Middle |
| lf:location-within-the-landform-element-T | Top |


## Strength of substrate material

**ANSIS Vocabulary Location:** subst:Material-strength

The strength of a specimen of soil substrate material may be crudely estimated in the field by striking it with the head-end or the pick-end of a geological hammer or by trying to cut it with a knife, and then referring to Table 32 (ASLS Field Handbook). These estimates refer to the unconfined (or uniaxial) compressive strength. The strength is that of the intact material rather than that of the mass, the strength of which has generally been reduced by the development of fractures and other phenomena.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:material-strength-M | Moderately strong rock |
| subst:material-strength-S | Strong rock |
| subst:material-strength-VS | Very strong rock |
| subst:material-strength-VW | Very weak rock |
| subst:material-strength-W | Weak rock |


## Biotic microrelief agents

**ANSIS Vocabulary Location:** ls:Microrelief-agent-biotic

The biotic agents causing the relief.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:biotic-microrelief-agent-A | Ant |
| ls:biotic-microrelief-agent-B | Bird |
| ls:biotic-microrelief-agent-M | Human |
| ls:biotic-microrelief-agent-N | Animal |
| ls:biotic-microrelief-agent-O | Other |
| ls:biotic-microrelief-agent-T | Termite |
| ls:biotic-microrelief-agent-V | Vegetation |


## Component of biotic relief

**ANSIS Vocabulary Location:** ls:Microrelief-component-biotic

The component of the biotic relief.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:biotic-microrelief-component-D | Depression |
| ls:biotic-microrelief-component-E | Elongate mound |
| ls:biotic-microrelief-component-H | Hole |
| ls:biotic-microrelief-component-L | Elongate depression |
| ls:biotic-microrelief-component-M | Mound |
| ls:biotic-microrelief-component-O | Other. |
| ls:biotic-microrelief-component-T | Terrace |


## Component of microrelief sampled

**ANSIS Vocabulary Location:** ls:Microrelief-component-sampled

Give the component of the microrelief in which the described soil profile is located.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:microrelief-component-D | Depression |
| ls:microrelief-component-E | Elongate mound |
| ls:microrelief-component-F | Flat |
| ls:microrelief-component-K | Hummock |
| ls:microrelief-component-L | Elongate depression |
| ls:microrelief-component-M | Mound |
| ls:microrelief-component-S | Shelf |


## Proportions of gilgai components

**ANSIS Vocabulary Location:** ls:Microrelief-proportions-gilgai

Give the proportions of gilgai components within the site, thus:

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:gilgai-microrelief-proportions-A | Equal mounds and depressions; no shelf present |
| ls:gilgai-microrelief-proportions-B | More mounds than depressions; no shelf present |
| ls:gilgai-microrelief-proportions-C | Fewer mounds than depressions; no shelf present |
| ls:gilgai-microrelief-proportions-D | Mound, shelf and depressions; shelf forms prominent part of gilgai |


## Type of gilgai microrelief

**ANSIS Vocabulary Location:** ls:Microrelief-type-gilgai

Gilgai is surface microrelief associated with soils containing shrink–swell clays. It does not include microrelief that apparently results from repeated freezing and thawing, solifluxion or faunal activity. Gilgai consist of mounds and depressions showing varying degrees of order, sometimes separated by a subplanar or slightly undulating surface.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:microrelief-A | Lattice gilgai |
| ls:microrelief-C | Crabhole gilgai |
| ls:microrelief-G | Contour gilgai |
| ls:microrelief-L | Linear gilgai |
| ls:microrelief-M | Melonhole gilgai |
| ls:microrelief-N | Normal gilgai |


## Type of hummocky microrelief

**ANSIS Vocabulary Location:** ls:Microrelief-type-hummocky

Hummocky microrelief is not thought to be associated with the shrink–swell process involved in gilgai microrelief.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:microrelief-D | Debil-debil |
| ls:microrelief-W | Swamp hummock |


## Type of other microrelief

**ANSIS Vocabulary Location:** ls:Microrelief-type-other

Type of other microrelief

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:microrelief-H | Spring hollow |
| ls:microrelief-I | Sinkhole |
| ls:microrelief-K | Karst microrelief |
| ls:microrelief-O | Other microrelief |
| ls:microrelief-P | Spring mound |
| ls:microrelief-R | Terracettes |
| ls:microrelief-S | Mass movement microrelief |
| ls:microrelief-T | Contour trench |
| ls:microrelief-U | Mound/depression microrelief |


## Mottle abundance

**ANSIS Vocabulary Location:** sp:Mottle-abundance

The percentage of mottles is estimated by eye using the chart in Figure 11 (ASLSFH3Ed) for comparison. 

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-abundance-0 | No mottles or other colour patterns |
| sp:mottle-abundance-1 | Very few (mottle abundance) |
| sp:mottle-abundance-2 | Few (mottle abundance) |
| sp:mottle-abundance-3 | Common (mottle abundance) |
| sp:mottle-abundance-4 | Many (mottle abundance) |


## Mottle colour

**ANSIS Vocabulary Location:** sp:Mottle-colour

This should be described in terms of Munsell or Revised Standard Soil colours, but abbreviated forms can be used

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-colour-B | Brown |
| sp:mottle-colour-D | Dark |
| sp:mottle-colour-G | Grey |
| sp:mottle-colour-L | Gley |
| sp:mottle-colour-O | Orange |
| sp:mottle-colour-P | Pale |
| sp:mottle-colour-R | Red |
| sp:mottle-colour-Y | Yellow |


## Mottle contrast

**ANSIS Vocabulary Location:** sp:Mottle-contrast

Mottle contrast

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-contrast-D | Distinct (mottle contrast) |
| sp:mottle-contrast-F | Faint (mottle contrast) |
| sp:mottle-contrast-P | Prominent (mottle contrast) |


## Mottle distinctness of boundaries

**ANSIS Vocabulary Location:** sp:Mottle-distinctness

Mottle distinctness of boundaries

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-boundary-C | Clear (mottle boundary) |
| sp:mottle-boundary-D | Diffuse (mottle boundary) |
| sp:mottle-boundary-S | Sharp (mottle boundary) |


## Mottle size

**ANSIS Vocabulary Location:** sp:Mottle-size

Measure mottle size (mm) along the greatest dimension, except in streaks or linear forms where width is measured.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-size-1 | Fine (mottle size) |
| sp:mottle-size-2 | Medium (mottle size) |
| sp:mottle-size-3 | Coarse (mottle size) |
| sp:mottle-size-4 | Very coarse (mottle size) |


## Mottle or colour pattern type

**ANSIS Vocabulary Location:** sp:Mottle-type

The type of mottle can suggest the origin of the mottles.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:mottle-type-M | Mottles |
| sp:mottle-type-X | Mottle type X |
| sp:mottle-type-Y | Mottle type Y |
| sp:mottle-type-Z | Mottle type Z |


## Cementation of pan

**ANSIS Vocabulary Location:** sp:Pans-cementation

Place a 30 mm diameter piece of the pan in water for 1 hour. If it slakes, it is uncemented; if not, it is cemented. The degree of cementation is assessed on the following scale after the 1 hour soaking in water.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:pans-cementation-0 | Uncemented |
| sp:pans-cementation-1 | Weakly cemented |
| sp:pans-cementation-2 | Moderately cemented |
| sp:pans-cementation-3 | Strongly cemented |
| sp:pans-cementation-4 | Very strongly cemented |


## Continuity of pan

**ANSIS Vocabulary Location:** sp:Pans-continuity

Continuity of pan

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:pans-continuity-B | Broken (pans continuity) |
| sp:pans-continuity-C | Continuous (pans continuity) |
| sp:pans-continuity-D | Discontinuous (pans continuity) |


## Type of pan

**ANSIS Vocabulary Location:** sp:Pans-type

Type of pan

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:pans-type-A | Alcrete (pans type) |
| sp:pans-type-C | Organic pan |
| sp:pans-type-D | Duripan |
| sp:pans-type-E | Ferricrete (pans type) |
| sp:pans-type-F | Fragipan |
| sp:pans-type-I | Thin ironpan |
| sp:pans-type-K | Calcrete (pans type) |
| sp:pans-type-L | Silcrete (pans type) |
| sp:pans-type-M | Manganiferous pan |
| sp:pans-type-N | Densipan |
| sp:pans-type-O | Other pans |
| sp:pans-type-R | Red-brown hardpan (pans type) |
| sp:pans-type-T | Ortstein |
| sp:pans-type-V | Cultivation pan |
| sp:pans-type-Z | Zero or no pan |


## Pedal soil grades

**ANSIS Vocabulary Location:** sp:Pedality-grade-pedal; sp:Pedality-grade-apedal

Pedal soils have observable peds and are divided into: sp:structure-pedality-grade-M, sp:structure-pedality-grade-S and sp:structure-pedality-grade-W. Apedal soils have no observable peds and are divided into: sp:structure-pedality-grade-G and sp:structure-pedality-grade-V

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:structure-pedality-grade-M | Moderate (structure pedality grade) |
| sp:structure-pedality-grade-S | Strong (structure pedality grade) |
| sp:structure-pedality-grade-W | Weak (structure pedality grade) |
| sp:structure-pedality-grade-G | Single grain |
| sp:structure-pedality-grade-V | Massive (structure pedality grade) |


## Size of peds

**ANSIS Vocabulary Location:** sp:Pedality-size

The average least dimension of peds is used to determine the class interval. Use figure 17. The least dimension is the vertical dimension for platy structure; the horizontal dimension for prismatic, columnar, blocky and polyhedral peds; the maximum separation of convex faces for lenticular peds; and the diameter for granular peds.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:structure-pedality-size-1 | < 2 mm |
| sp:structure-pedality-size-2 | 2-5 mm |
| sp:structure-pedality-size-3 | 5-10 mm |
| sp:structure-pedality-size-4 | 10-20 mm |
| sp:structure-pedality-size-5 | 20-50 mm |
| sp:structure-pedality-size-6 | 50-100 mm |
| sp:structure-pedality-size-7 | 100-200 mm |
| sp:structure-pedality-size-8 | 200-500 mm |
| sp:structure-pedality-size-9 | > 500 mm |


## Type of pedality

**ANSIS Vocabulary Location:** sp:Pedality-type

The types of structure are illustrated in diagrammatic form. See figure 17.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:structure-pedality-type-AB | Angular blocky |
| sp:structure-pedality-type-CA | Cast |
| sp:structure-pedality-type-CO | Columnar |
| sp:structure-pedality-type-GR | Granular |
| sp:structure-pedality-type-LE | Lenticular |
| sp:structure-pedality-type-PL | Platy (structure pedality) |
| sp:structure-pedality-type-PO | Polyhedral |
| sp:structure-pedality-type-PR | Prismatic |
| sp:structure-pedality-type-SB | Subangular blocky |


## Abundance of very fine, fine, medium and coarse macropores

**ANSIS Vocabulary Location:** sp:Pore-abundance-fine; sp:Pore-abundance-coarse

Abundance of very fine and fine macropores (less than 2mm diameter), and medium and coarse macropores (greater than 2 mm diameter).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:voids-macropores-abundance-0 | No macropores |
| sp:voids-macropores-abundance-1 | Few fine or very fine macropores |
| sp:voids-macropores-abundance-2 | Common fine or very fine macropores |
| sp:voids-macropores-abundance-3 | Many fine or very fine macropores |
| sp:voids-macropores-abundance-4 | Few medium or coarse macropores |
| sp:voids-macropores-abundance-5 | Common medium or coarse macropores |
| sp:voids-macropores-abundance-6 | Many medium or coarse macropores |


## Diameter of macropores

**ANSIS Vocabulary Location:** sp:Pore-diameter

Diameter of macropores Use Figure 18 as a guide to average diameter

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:voids-macropores-diameter-1 | Very fine (voids macropores) |
| sp:voids-macropores-diameter-2 | Fine (voids macropores) |
| sp:voids-macropores-diameter-3 | Medium (voids macropores) |
| sp:voids-macropores-diameter-4 | Coarse (voids macropores) |


## Type of soil observation

**ANSIS Vocabulary Location:** sp:Profile-construction

The soil profile may be described using several types of observation.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:observation-type-A | Auger boring |
| sp:observation-type-C | Relatively undisturbed soil core |
| sp:observation-type-E | Existing vertical exposure |
| sp:observation-type-P | Soil pit |


## Abundance of rock outcrop

**ANSIS Vocabulary Location:** ls:Rock-outcrop-abundance

Abundance of rock outcrop.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:rock-outcrop-abundance-0 | No rock outcrop |
| ls:rock-outcrop-abundance-1 | Very slightly rocky |
| ls:rock-outcrop-abundance-2 | Slightly rocky |
| ls:rock-outcrop-abundance-3 | Rocky |
| ls:rock-outcrop-abundance-4 | Very rocky |
| ls:rock-outcrop-abundance-5 | Rockland |


## Relative inclination of slope elements

**ANSIS Vocabulary Location:** lf:Relative-inclination

Although lower slopes are often gentler than upper slopes, they need not be so (Figure 1i). A separate morphological attribute expresses the relative inclination of adjacent landform elements in a toposequence.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:relative-inclination-of-slope-elements-A | Maximal |
| lf:relative-inclination-of-slope-elements-I | Minimal |
| lf:relative-inclination-of-slope-elements-N | Waning |
| lf:relative-inclination-of-slope-elements-X | Waxing |


## Relief

**ANSIS Vocabulary Location:** lf:Relief

Relief is defined as the difference in elevation between the high and low points of a land surface. Its estimation will be made easier by visualising two surfaces of accordance that are planar or gently curved, one touching the major crests of a landform pattern, and the other passing through the major depressions. The average vertical separation of the two surfaces is a measure of the relief. Make this estimation at a field site, either visually or by using a map, and express it in metres.
Relief is the definitive characteristic for the terms mountains, hills, low hills, rises and plains when used as types of erosional landform pattern (Table 5). The class boundaries, shown in Tables 5 and 6, are set at 300 m, 90 m, 30 m and 9 m. These class limits and the class names are similar to those used by Löffler (1974), and are broadly compatible with those of Löffler and Ruxton (1969).
Table 6 lists types of landform pattern defined in the glossary according to their typical relief class. Those types for which the relief class is definitive are in italics.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:relief-class-H | High |
| lf:relief-class-L | Low |
| lf:relief-class-M | Very high |
| lf:relief-class-P | Extremely low |
| lf:relief-class-R | Very low |


## Alteration

**ANSIS Vocabulary Location:** subst:Rock-alteration

Substrate materials may be so extensively altered (as in deep weathering profiles) that it may be difficult or impossible to determine their original nature. Certain constituents may be either depleted or enriched. Thus, in many laterite profiles, some horizons are ferruginised, partially ferruginised and partially kaolinised, and the pallid zone kaolinised. Silicification may also be associated with deep weathering profiles although not exclusively so; for instance, some limestones may be variably silicified. In contrast, calcification, which is widespread in parts of southern Australia, is not usually associated with deep weathering.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:alteration-F | Ferruginised |
| subst:alteration-K | Calcified |
| subst:alteration-L | Kaolinised |
| subst:alteration-O | Other |
| subst:alteration-S | Silicified |


## Artificially hardened materials

**ANSIS Vocabulary Location:** subst:Rock-genesis-hardened-artificial

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-AT | Other artificially hardened materials |
| subst:genesis-CN | Concrete |
| subst:genesis-ST | Stabilised soil |


## Chemically hardened materials

**ANSIS Vocabulary Location:** subst:Rock-genesis-hardened-chemical

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-AC | Alcrete (bauxite) |
| subst:genesis-FC | Ferricrete |
| subst:genesis-KC | Calcrete |
| subst:genesis-LC | Silcrete |
| subst:genesis-PC | Porcellanite |
| subst:genesis-RB | Red-brown hardpan |


## Evaporites

**ANSIS Vocabulary Location:** subst:Rock-genesis-hardened-evaporite

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-EV | Evaporite |
| subst:genesis-GY | Gypsum |
| subst:genesis-HA | Halite (rock salt) |


## Sediments (unconsolidated)

**ANSIS Vocabulary Location:** subst:Rock-genesis-sediments

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-AL | Alluvium |
| subst:genesis-BE | Beach sediment |
| subst:genesis-CD | Creep deposit |
| subst:genesis-CO | Colluvium |
| subst:genesis-ED | Eolian sediment |
| subst:genesis-ES | Eolian sand |
| subst:genesis-FI | Fill |
| subst:genesis-GY | Gypsum |
| subst:genesis-LA | Lacustrine sediment |
| subst:genesis-LD | Landslide deposit |
| subst:genesis-LO | Loess |
| subst:genesis-MA | Marine sediment |
| subst:genesis-MD | Mudflow deposit |
| subst:genesis-PA | Parna |
| subst:genesis-SE | Scree |
| subst:genesis-SH | Sheet flow deposit |
| subst:genesis-TI | Till |
| subst:genesis-VA | Volcanic ash |


## Unweathered rocks of the bedrock zone

**ANSIS Vocabulary Location:** subst:Rock-genesis-unweathered

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-ET | Eolianite |
| subst:genesis-IG | Igneous rocks |
| subst:genesis-IN | Ignimbrite |
| subst:genesis-ME | Metamorphic rocks |
| subst:genesis-PL | Plutonic rocks |
| subst:genesis-SC | Chemical and organic sedimentary rocks |
| subst:genesis-SD | Detrital sedimentary rocks |
| subst:genesis-SP | Pyroclastic rocks |
| subst:genesis-SR | Sedimentary rocks |
| subst:genesis-VO | Volcanic rocks |


## Weathered rocks

**ANSIS Vocabulary Location:** subst:Rock-genesis-weathered

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:genesis-DR | Decomposed rock |
| subst:genesis-PW | Partially weathered rock |
| subst:genesis-SA | Saprolite |


## Root abundance

**ANSIS Vocabulary Location:** sp:Root-abundance

Number of roots per 0.01 m2 (100 mm × 100 mm)

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:roots-abundance-0 | No roots |
| sp:roots-abundance-1 | Few (roots abundance) |
| sp:roots-abundance-2 | Common (roots abundance) |
| sp:roots-abundance-3 | Many (roots abundance) |
| sp:roots-abundance-4 | Abundant (roots abundance) |


## Root size

**ANSIS Vocabulary Location:** sp:Root-size

The size (diameter) of roots observed in the horizon in mm

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:roots-size-1 | Very fine (roots size) |
| sp:roots-size-2 | Fine (roots size) |
| sp:roots-size-3 | Medium (roots size) |
| sp:roots-size-4 | Coarse (roots size) |


## Runoff

**ANSIS Vocabulary Location:** ls:Runoff

Runoff is the relative rate at which water runs off the soil surface. It is largely determined by slope, surface cover and soil infiltration rate. 

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| ls:runoff-0 | No runoff |
| ls:runoff-1 | Very slow |
| ls:runoff-2 | Slow |
| ls:runoff-3 | Moderately rapid |
| ls:runoff-4 | Rapid |
| ls:runoff-5 | Very rapid |


## Abundance of segregations

**ANSIS Vocabulary Location:** sp:Segregations-abundance

Abundance of segregations. Use figure 11 as a guide.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-abundance-0 | No segregations |
| sp:segregations-abundance-1 | Very few (segregations abundance) |
| sp:segregations-abundance-2 | Few (segregations abundance) |
| sp:segregations-abundance-3 | Common (segregations abundance) |
| sp:segregations-abundance-4 | Many (segregations abundance) |
| sp:segregations-abundance-5 | Very many (segregations abundance) |


## Form of segregations

**ANSIS Vocabulary Location:** sp:Segregations-form

Form of segregations

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-form-C | Concretions |
| sp:segregations-form-F | Fragments |
| sp:segregations-form-L | Laminae |
| sp:segregations-form-N | Nodules (segregations) |
| sp:segregations-form-R | Root linings |
| sp:segregations-form-S | Soft segregations |
| sp:segregations-form-T | Tubules |
| sp:segregations-form-V | Veins |
| sp:segregations-form-X | Crystals |


## Magnetic attributes of segregations

**ANSIS Vocabulary Location:** sp:Segregations-magnetic-attributes

attraction to surface of hand-held magnet

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-magnetic-M | Magnetic |
| sp:segregations-magnetic-N | Non-magnetic |


## Nature of segregations

**ANSIS Vocabulary Location:** sp:Segregations-nature

Nature of segregations

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-nature-A | Aluminous |
| sp:segregations-nature-E | Earthy |
| sp:segregations-nature-F | Ferruginous |
| sp:segregations-nature-G | Ferruginous–organic |
| sp:segregations-nature-H | Organic |
| sp:segregations-nature-K | Calcareous |
| sp:segregations-nature-L | Argillaceous |
| sp:segregations-nature-M | Manganiferous |
| sp:segregations-nature-N | Ferromanganiferous |
| sp:segregations-nature-O | Other (segregations nature) |
| sp:segregations-nature-S | Sulphurous |
| sp:segregations-nature-U | Unidentified |
| sp:segregations-nature-Y | Gypseous |
| sp:segregations-nature-Z | Saline (segregations nature) |


## Size of segregations

**ANSIS Vocabulary Location:** sp:Segregations-size

Approximately equidimensional segregations (concretions, nodules) are measured in the greatest dimension. Segregations where one dimension is much greater than the other two (tubules, root linings, veins, laminae) are measured in the least dimension

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-size-1 | Fine (segregations size) |
| sp:segregations-size-2 | Medium (segregations size) |
| sp:segregations-size-3 | Coarse (segregations size) |
| sp:segregations-size-4 | Very coarse (segregations size) |
| sp:segregations-size-5 | Extremely coarse (segregations size) |


## Strength of segregations

**ANSIS Vocabulary Location:** sp:Segregations-strength

Strength may be recorded where appropriate

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:segregations-strength-1 | Weak (segregations strength) |
| sp:segregations-strength-2 | Strong (segregations strength) |


## Class of slope

**ANSIS Vocabulary Location:** lf:Slope-class

Slope classes are defined in Table 2. The optional word ‘inclined’ is used to distinguish slope from other attributes, for example ‘gently inclined footslope’ from ‘gently undulating rises’, and ‘moderately inclined hillslope’ from ‘moderately spaced streams’.
The class boundaries given in Table 2, and repeated in Table 4, are simply boundaries separating slope terms in common use, adjusted to regular logarithmic intervals. They do not refer to observed natural clustering of slope values, since such clustering has not been shown to occur; nor do they relate precisely to boundary criteria for land use, which vary arbitrarily between organisations and which may change with advancing technology.
It may sometimes be advantageous to split each of the classes ‘very gently inclined’, ‘gently inclined’ and ‘moderately inclined’ into two levels, the appropriate boundary values being 1.8%, 5.6% and 18%.
There may also be compelling reasons for using other schemes of slope classes. However, schemes that do not have constant class widths from low to high slope values can lead to problems in subsequent statistical work.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:slope-class-CL | Cliffed |
| lf:slope-class-GE | Gently inclined |
| lf:slope-class-LE | level |
| lf:slope-class-MO | Moderately inclined |
| lf:slope-class-PR | Precipitous |
| lf:slope-class-ST | Steep |
| lf:slope-class-VG | Very gently inclined |
| lf:slope-class-VS | Very steep |


## Modal slope

**ANSIS Vocabulary Location:** lf:Slope-modal

Modal slope is defined as the most common class of slope occurring in a landform pattern. Where slope classes have been obtained by systematic sampling, define the classes using equal increments on a scale of the logarithm of the slope tangent, a procedure intended to normalise frequency distributions of observed slope (Speight 1971). Where the most common slope class is estimated by direct observation, it is thought that the estimate will compare with that calculated using the log-normal model.
Modal slope class determines the use of certain adjectives applied to landform patterns that are characterised by alternating crests and depressions. These are: rolling for moderate modal slopes (10–32%); undulating for gentle slopes (3–10%); and gently undulating for very gentle slopes (1–3%) (compare with Soil Survey Staff 1951, pages 161–165). The other slope classes, precipitous, very steep, steep and level, are to be applied as they stand. The terminology for simple erosional landform patterns based on relief and modal slope is given in Table 5.
Table 5 defines the category badlands by various combinations of high slope values and low relief values. These combinations imply extremely close spacing of streams or valleys. Specifically, if one assumes a sawtooth terrain profile, the valley spacing implied is less than 100 m in areas with 50 m relief and less than 30 m in areas with 5 m relief; these values appear to accord with usage.
Table 7 lists types of landform pattern in order of their typical class of modal slope. This table should not be regarded as definitive, for slope within each type of landform pattern may vary widely.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:relief-class-H | High |
| lf:relief-class-L | Low |
| lf:relief-class-M | Very high |
| lf:relief-class-P | Extremely low |
| lf:relief-class-R | Very low |


## Means of evaluation of slope

**ANSIS Vocabulary Location:** lf:Slope-procedure

Means of evaluation of slope

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| lf:slope-evaluation-A | Abney level or clinometer and tape |
| lf:slope-evaluation-E | Estimate |
| lf:slope-evaluation-P | Contour plan at 1:10 000 or larger scale |
| lf:slope-evaluation-T | Tripod-mounted instrument and staff |


## Permeability

**ANSIS Vocabulary Location:** sp:Soil-permeability

Permeability is independent of climate and drainage, and – as applied to a soil – is controlled by the potential to transmit water (saturated hydraulic conductivity, Ks) of the least permeable layer in the soil. Therefore it is inferred from attributes of the soil such as structure, texture, porosity, cracks and shrink–swell properties. The rate of transmission of water in the profile is based on the assumption that loss by evapotranspiration is minimal. The Ks ranges are compatible with those of Nowland in Canada, as reported by McKeague et al. (1982).

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:soil-water-permeability-1 | Very slowly permeable |
| sp:soil-water-permeability-2 | Slowly permeable |
| sp:soil-water-permeability-3 | Moderately permeable |
| sp:soil-water-permeability-4 | Highly permeable |


## Soil Water Drainage

**ANSIS Vocabulary Location:** sp:Site-drainage

Drainage is a useful term to summarise local soil wetness conditions, that is, it provides a statement about soil and site drainage likely to occur in most years. It is affected by a number of attributes, both internal and external, that may act separately or together. Internal attributes include soil structure, texture, porosity, hydraulic conductivity, and water-holding capacity, while external attributes are source and quality of water, evapotranspiration, gradient and length of slope, and position in the landscape.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:soil-water-drainage-1 | very poorly drained |
| sp:soil-water-drainage-2 | poorly drained |
| sp:soil-water-drainage-3 | imperfectly drained |
| sp:soil-water-drainage-4 | moderately well drained |
| sp:soil-water-drainage-5 | well drained |
| sp:soil-water-drainage-6 | rapidly drained |


## Soil water status

**ANSIS Vocabulary Location:** sp:Soil-water-status

Give soil water status of the soil at the time of description.
It may also be relevant to note the weather conditions immediately prior to examination of the soil if these are known, for example a soil may be wet because of local rain or from seepage.
The following guidelines may be used as a crude approximation of soil water status:

Dry is below wilting point. Material becomes darker or has lower colour value when moistened.
Moderately moist is the drier half of the available moisture range.
Moist is the wetter half of the available moisture range.
Wet is at, or exceeding, field capacity. Will wet and/or stick to fingers when moulded.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:soil-water-status-D | Dry (soil water status) |
| sp:soil-water-status-M | Moist (soil water status) |
| sp:soil-water-status-T | Moderately moist (soil water status) |
| sp:soil-water-status-W | Wet (soil water status) |


## Compound pedality

**ANSIS Vocabulary Location:** sp:structure-pedality-compound

Compound pedality occurs where large peds part along natural planes of weakness to form smaller peds, which may again part to smaller peds, and so on to the smallest or primary peds.
Primary peds are the simplest peds occurring in soil material; they cannot be divided into smaller peds, but may be packed together to form compound peds of a higher level of organisation (Brewer 1964).
The order of peds and relationship of one to the other is important and may be described as the larger peds parting to the smaller and further where necessary. For example, 'strong 50-100 mm columnar, parting to moderate 20-50 mm prismatic, parting to moderate
10-20 mm angular blocky'. The word 'parting' and not 'breaking' is used. The term 'breaking' is used when soil is fractured along planes other than natural planes of weakness.
1	Largest peds (in the type of soil observation described), parting to
2	Next size peds, parting to
3	Next size peds, ... and further, if required, to the primary ped.

> No skos:members found.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| xx:placeholder | placeholder value |


## Confidence that substrate is parent material

**ANSIS Vocabulary Location:** subst:Confidence

The observer should state the degree of confidence that the observed substrate material is in fact the parent material of the observed soil profile or the major part of that profile, that is, of the B horizon.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:confidence-certain | certain |
| subst:confidence-probable | probable |
| subst:confidence-doubtful | doubtful |
| subst:confidence-not-parent | not-parent |


## Spacing of discontinuities

**ANSIS Vocabulary Location:** subst:Substrate-discontinuity-spacing

Physical weathering opens up fissures or joints that reduce the strength of the rock mass relative to that of the intact rock material.  These fissures generally increase in number towards the land surface.  The following categories of discontinuity spacing apply (Deere 1968, Selby 1982):

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:discontinuity-spacing-B | blocky; moderately jointed. |
| subst:discontinuity-spacing-C | crushed or shattered. |
| subst:discontinuity-spacing-F | fractured; intensely jointed. |
| subst:discontinuity-spacing-M | massive; few joints. |
| subst:discontinuity-spacing-S | solid; virtually unjointed |


## Grain size

**ANSIS Vocabulary Location:** subst:Substrate-grain-size

It is informative to estimate the size of the most common particles of a substrate material whether the material is thought to be of sedimentary, metamorphic or igneous origin.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:grain-size-1 | <0.06 mm |
| subst:grain-size-2 | 0.06-2 mm |
| subst:grain-size-3 | >2 mm |


## Mineral composition

**ANSIS Vocabulary Location:** subst:Substrate-mineral-composition

Make provision for recording one dominant mineral and one or two minor minerals, as identified by inspection of the hand specimen.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| subst:mineral-composition-C | Carbonaceous material |
| subst:mineral-composition-D | Dark minerals |
| subst:mineral-composition-F | Feldspar |
| subst:mineral-composition-G | Glauconite |
| subst:mineral-composition-K | Carbonates (react with 1-molar HCl) |
| subst:mineral-composition-L | Clays (argillaceous) |
| subst:mineral-composition-M | Mica |
| subst:mineral-composition-Q | Quartz |
| subst:mineral-composition-S | Sesquioxides |
| subst:mineral-composition-Y | Gypsum |


## Condition of surface soil when dry

**ANSIS Vocabulary Location:** sp:Surface-condition

Many surface soils have a characteristic appearance when dry. Because surface conditions are often relevant to the use of the soil and indicative of particular kinds of soil, every effort should be made to observe the surface condition in the dry state. The surface conditions are not necessarily mutually exclusive:

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:surfacecondition-C | Surface crust |
| sp:surfacecondition-F | Firm (surface condition) |
| sp:surfacecondition-G | Cracking |
| sp:surfacecondition-H | Hard setting |
| sp:surfacecondition-L | Loose (surface condition) |
| sp:surfacecondition-M | Self-mulching |
| sp:surfacecondition-O | Other (surface condition) |
| sp:surfacecondition-P | Poached |
| sp:surfacecondition-R | Recently cultivated |
| sp:surfacecondition-S | Soft |
| sp:surfacecondition-T | Trampled |
| sp:surfacecondition-X | Surface flake |
| sp:surfacecondition-Y | Cryptogam surface |
| sp:surfacecondition-Z | Saline (surface condition) |


## Water repellence

**ANSIS Vocabulary Location:** sp:Water-repellence

Water repellence of some soils, usually sandy, is caused by a series of long-chain polymethylene waxes, made up of acids, alcohols and esters, attached to the sand grains (Ma’shum et al. 1988). These soils occur Australia-wide but are more widespread in southern Australia (Wetherby 1984, McGhie and Posner 1980). Degree of repellence is assessed by determining the concentration of ethanol required to wet the sand in 10 seconds (King 1981). An abbreviated form of this method is recommended for routine field situations.

| ID/JSON Value | Preferred Label |
| ---------- | --------------- |
| sp:water-repellence-N | Non water repellent |
| sp:water-repellence-R | Water repellent |
| sp:water-repellence-S | Strongly water repellent |

