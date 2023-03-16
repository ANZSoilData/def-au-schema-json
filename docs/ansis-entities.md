# ANSIS Soil Domain Entity Schema
**JSON Schema Location:** https://anzsoildata.github.io/def-au-schema-json/schema/domain/2023-06-30/entities.json

JSON Schema definitions of the complete list of entities (features in GIS speak) defined in or imported by the ANSIS Domain Ontology.

> Instances of entities can be created/validated using the entity-instance and entity-instance-collection schema.

## Core Entities

### ANSIS Soil Site - `ansis:SoilSite`

A site where samples, observations, and treatments of soil are carried out.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| hasGeometry | 1..* | sosa:ObservableProperty; geo:wktLiteral | The default geometry to be used in spatial calculations. It is Usually the most detailed geometry. |
| isSampleOf | 0..1 |  | template |
| depthFreeWater | 0..1 | sosa:ObservableProperty; qudt:QuantityValue | Depth to free water at the site of soil observation, either above or below the soil surface, excluding litter and living vegetation. Positive values indicate water above the soil surface. Negative values indicate water below the soil surface. |
| designSite | 0..1 | ansis:SoilSite-design | overall design of sampling at the site e.g. ASLS|grid|transect |
| designSurvey | 0..1 | ansis:Survey-design | overall design of soil or landscape survey e.g. free|grid|stratified|miscellaneous |
| disturbance | 0..1 | sosa:ObservableProperty; skos:Concept | disturbance of site |
| drainage | 0..1 | sosa:ObservableProperty; skos:Concept | Drainage of site or profile. |
| hasErosion | 0..1 | ansis:Erosion | link to description of erosion |
| hasLandCover | 0..1 | ansis:LandManagement | link to description of land cover |
| hasLandManagement | 0..1 | ansis:LandManagement | link to description of land management |
| hasLandSurface | 0..1 | ansis:LandSurface | link to description of land surface |
| hasLandUse | 0..* | ansis:LandUse | link to description of land use |
| hasLandform | 0..1 | ansis:Landform | link to description of landform |
| hasMicrorelief | 0..1 | ansis:Microrelief | link to description of microrelief at the site |
| hasOutcrop | 0..1 | ansis:Outcrop | link to description of rock outcrop at this entity |
| heightDrainage | 0..1 | sosa:ObservableProperty; qudt:QuantityValue | vertical extent of drainage |
| locationInElement | 0..1 | sosa:ObservableProperty; skos:Concept | location within landform element |
| locationInToposequence | 0..1 | sosa:ObservableProperty; skos:Concept | location within a toposequence |
| purpose | 0..1 | ansis:Profile-purpose; ansis:Site-purpose | purpose of or reason for activity |
| relatedLandSurveySite | 0..1 | ansis:LandSurveySite | link to a land survey site related to this context |
| relatedProfile | 0..* | ansis:SoilProfile | Link to a soil profile related to this context. |
| relatedProject | 1..* | ansis:Project | link to project that supported this activity |
| relatedSite | 0..1 | ansis:SoilSite | link to a soil site related to this context |
| relatedSoilBody | 0..1 | ansis:SoilBody | link to a soil body related to this context |
| relatedSoilSurface | 0..1 | ansis:SoilSurface | soil surface of this entity |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Soil Profile - `ansis:SoilProfile`

A soil profile is a vertical section of a soil from the soil surface through all its horizons to parent material, other consolidated substrate material or selected depth in unconsolidated material.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| depth | 1..1 | sosa:ObservableProperty; qudt:QuantityValue |  |
| drainage | 0..1 | sosa:ObservableProperty; skos:Concept | Drainage of site or profile. |
| procedure | 1..1 |  | Relation between an Observation and the Sensor which made the Observations. |
| purpose | 0..1 | ansis:Profile-purpose; ansis:Site-purpose | purpose of or reason for activity |
| hasGeometry | 1..1 | sosa:ObservableProperty; geo:wktLiteral | The default geometry to be used in spatial calculations. It is Usually the most detailed geometry. |
| hasRoots | 0..1 | ansis:Roots | link to description of roots |
| hasSubstrate | 0..1 | ansis:Substrate | link to description of substrate |
| relatedHorizon | 0..1 | ansis:SoilHorizon | related soil horizon within a soil body or sample, or associated with a contact |
| relatedLayer | 0..* | ansis:SoilLayer | related soil layer within a soil body or profile |
| relatedSample | 0..1 | ansis:SoilSample | link to a sample related to this context |
| relatedSite | 1..1 | ansis:SoilSite | link to a soil site related to this context |
| relatedSoilSurface | 0..1 | ansis:SoilSurface | soil surface of this entity |
### ANSIS Soil Body - `ansis:SoilBody`

Part of the soil cover that is delineated at a scale useful for an application, and is homogeneous with regard to properties and/or spatial patterns.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| classification | 0..* | sosa:ObservableProperty; ansis:SoilClassification | classification of the soil body or profile |
| hasGeometry | 0..* | sosa:ObservableProperty; geo:wktLiteral | The default geometry to be used in spatial calculations. It is Usually the most detailed geometry. |
| hasLandManagement | 0..1 | ansis:LandManagement | link to description of land management |
| hasLandSurface | 0..1 | ansis:LandSurface | link to description of land surface |
| hasLandUse | 0..* | ansis:LandUse | link to description of land use |
| hasLandform | 0..1 | ansis:Landform | link to description of landform |
| hasMicrorelief | 0..1 | ansis:Microrelief | link to description of microrelief at the site |
| hasSubstrate | 0..1 | ansis:Substrate | link to description of substrate |
| relatedHorizon | 0..1 | ansis:SoilHorizon | related soil horizon within a soil body or sample, or associated with a contact |
| relatedLayer | 0..* | ansis:SoilLayer | related soil layer within a soil body or profile |
| relatedSample | 0..1 | ansis:SoilSample | link to a sample related to this context |
| relatedSite | 0..1 | ansis:SoilSite | link to a soil site related to this context |
| relatedSoilSurface | 0..1 | ansis:SoilSurface | soil surface of this entity |
### ANSIS Soil Layer - `ansis:SoilLayer`

Region within a soil body usually observed as a specified depth interval within a profile.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| depthUpper | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the top of the element |
| depthLower | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the base of the element |
| permeability | 0..1 | sosa:ObservableProperty; skos:Concept | rate of flow of liquid through the material |
| texture | 0..* | sosa:ObservableProperty; skos:Concept | material texture, in terms of particle size distribution and component materials |
| colour | 0..* |  | link to description of colour |
| hasCoarseFragments | 0..* | ansis:CoarseFragments | link to description of coarse fragments |
| hasCracks | 0..* | ansis:Cracks | link to description of cracks |
| hasCutans | 0..* | ansis:Cutans | link to description of cutans |
| hasMottles | 0..* | ansis:Mottles | link to description of mottles and other colour patterns |
| hasPans | 0..* | ansis:Pans | link to description of pans |
| hasPores | 0..* | ansis:Pores | link to description of macropores |
| hasRoots | 0..* | ansis:Roots | link to description of roots |
| hasSegregations | 0..* | ansis:Segregations | link to description of segregations |
| hasStrength | 0..1 | sosa:ObservableProperty; ansis:SoilStructure | internal arrangement of elements of the material or entity |
| relatedSample | 0..* | ansis:SoilSample | link to a sample related to this context |
| relatedSoilBody | 1..1 | ansis:SoilBody | link to a soil body related to this context |
| chemistry | 0..1 | sosa:Observation |  |
| physical | 0..1 | sosa:Observation |  |
| biological | 0..1 | sosa:Observation |  |
### ANSIS Soil Horizon - `ansis:SoilHorizon`

Soil layer which is compositionally and/or structurally homogeneous, delineated by pedological boundaries.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| designation | 1..1 | sosa:ObservableProperty; ansis:HorizonDesignation | designation of soil horizon with the sequence composing the Profile or Soil Body |
| depthUpper | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the top of the element |
| depthLower | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the base of the element |
| permeability | 0..1 | sosa:ObservableProperty; skos:Concept | rate of flow of liquid through the material |
| texture | 0..* | sosa:ObservableProperty; skos:Concept | material texture, in terms of particle size distribution and component materials |
| colour | 0..* |  | link to description of colour |
| hasCoarseFragments | 0..* | ansis:CoarseFragments | link to description of coarse fragments |
| hasCracks | 0..* | ansis:Cracks | link to description of cracks |
| hasCutans | 0..* | ansis:Cutans | link to description of cutans |
| hasMottles | 0..* | ansis:Mottles | link to description of mottles and other colour patterns |
| hasPans | 0..* | ansis:Pans | link to description of pans |
| hasPores | 0..* | ansis:Pores | link to description of macropores |
| hasRoots | 0..* | ansis:Roots | link to description of roots |
| hasSegregations | 0..* | ansis:Segregations | link to description of segregations |
| hasStrength | 0..1 | sosa:ObservableProperty; ansis:SoilStructure | internal arrangement of elements of the material or entity |
| relatedSample | 0..* | ansis:SoilSample | link to a sample related to this context |
| relatedSoilBody | 1..1 | ansis:SoilBody | link to a soil body related to this context |
| chemistry | 0..1 | sosa:Observation |  |
| physical | 0..1 | sosa:Observation |  |
| biological | 0..1 | sosa:Observation |  |
### ANSIS Soil Sample - `ansis:SoilSample`

Sample of soil or soil entity. Sample is a key class in the context of observations. The sample is an intermediate object, which is intended to be representative of the entity that we wish to characterize. The relationship of the sample to the ultimate entity-of-interest is recorded through the following properties: - `sosa:isSampleOf` to indicate the entity that this sample represents; - `ansis:component` (if necessary) to indicate which component of the entity the observation related to, such as coarse-fragments or mottles; - `ansis:relatedProfile` to indicate the 'profile' where it is taken (this may be a formal, complete profile, or an informal profile such as a shallow auger or shovel location); - `ansis:depth-lower` + `ansis:depth-upper` (if necessary) to indicate the precise depth range within the profile where the sample was taken.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| hasGeometry | 0..1 | sosa:ObservableProperty; geo:wktLiteral | The default geometry to be used in spatial calculations. It is Usually the most detailed geometry. |
| depthLower | 0..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the top of the element |
| depthUpper | 0..1 | sosa:ObservableProperty; qudt:QuantityValue | depth from local surface to the base of the element |
| component | 0..1 | sosa:ObservableProperty; skos:Concept | type of component element |
| isSampleOf | 1..1 |  | template |
| relatedProfile | 1..* | ansis:SoilProfile | Link to a soil profile related to this context. |
### ANSIS Land Survey Site - `ansis:LandSurveySite`

A Site established to make observations of landscape entities.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| hasGeometry | 1..* | sosa:ObservableProperty; geo:wktLiteral | The default geometry to be used in spatial calculations. It is Usually the most detailed geometry. |
| hasErosion | 0..1 | ansis:Erosion | link to description of erosion |
| hasLandCover | 0..1 | ansis:LandManagement | link to description of land cover |
| hasLandManagement | 0..1 | ansis:LandManagement | link to description of land management |
| hasLandSurface | 0..1 | ansis:LandSurface | link to description of land surface |
| hasLandUse | 0..* | ansis:LandUse | link to description of land use |
| hasLandform | 0..1 | ansis:Landform | link to description of landform |
| hasOutcrop | 0..1 | ansis:Outcrop | link to description of rock outcrop at this entity |
| relatedLandsurveySite | 0..1 | ansis:LandSurveySite | link to a land survey site related to this context |
### ANSIS Soil Surface - `ansis:SoilSurface`

The surface of the soil body.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| conditionWhenDry | 0..1 | sosa:ObservableProperty; skos:Concept | surface condition when dry |
| hasCoarseFragments | 0..1 | ansis:CoarseFragments | link to description of coarse fragments |
| relatedSoilBody | 0..1 | ansis:SoilBody | link to a soil body related to this context |
### ANSIS Substrate - `ansis:Substrate`

Observed or inferred materials and masses of earth or rock that do not show pedological development. They are not soils, but typically underlie them. The substrate includes the R horizon and that part of the C horizon that shows no pedological development, but excludes the solum, buried soil horizons (including D horizons), and pans. The substrate beneath a soil profile may or may not be the parent material of the soil.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| distance | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | spatial separation of objects |
| depth | 1..1 | sosa:ObservableProperty; qudt:QuantityValue |  |
| confidence | 0..1 | skos:Concept | confidence in assessment |
| relatedSample | 0..1 | ansis:SoilSample | link to a sample related to this context |
| relatedSoilBody | 0..1 | ansis:SoilBody | link to a soil body related to this context |
### ANSIS Treatment - `ansis:Treatment`

Intervention or treatment. Type of sosa:Actuation.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| actsOnProperty | 0..1 |  | Relation between an Actuation and the property of a FeatureOfInterest it is acting upon. |
| hasFeatureOfInterest | 0..1 |  | A relation between an Observation and the entity whose quality was observed, or between an Actuation and the entity whose property was modified, or between an act of Sampling and the entity that was sampled. |
| phenomenonTime | 0..1 |  | The time that the Result of an Observation, applies to the FeatureOfInterest. Not necessarily the same as the resultTime. May be an interval or an instant, or some other compound temporal entity [owl-time]. |
| relatedActivity | 0..* | prov:Activity; sosa:Actuation; sosa:Observation; sosa:Sampling; ansis:SiteVisit; ansis:Treatment | link to an activity related to this context |
## Other Entities

### ANSIS Coarse Fragments - `ansis:CoarseFragments`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
| shape | 0..1 | sosa:ObservableProperty; skos:Concept | geometry of entity or entity boundary - in the context of a soil horizon, this refers to the shape of the lower boundary |
### ANSIS Cracks - `ansis:Cracks`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Cutans - `ansis:Cutans`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
### ANSIS  - `ansis:Erosion`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| degree | 0..1 | sosa:ObservableProperty; skos:Concept | degree or severity or intensity of phenomenon |
### ANSIS Inundation - `ansis:Inundation`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| frequency | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | temporal frequency of event or phenomenon |
### ANSIS Land Cover - `ansis:LandCover`

Land cover, including vegetation.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Land Management - `ansis:LandManagement`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Land Surface - `ansis:LandSurface`

Surface landscape features of a site.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| aspect | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | direction or azimuth that a terrain surface faces |
| elevation | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | elevation of element above a datum (usually MSL) |
| hasCoarseFragments | 0..1 | ansis:CoarseFragments | link to description of coarse fragments |
| hasOutcrop | 0..1 | ansis:Outcrop | link to description of rock outcrop at this entity |
| hasErosion | 0..1 | ansis:Erosion | link to description of erosion |
| hasMicrorelief | 0..1 | ansis:Microrelief | link to description of microrelief at the site |
| hasInundation | 0..1 | ansis:Inundation | link to description of inundation |
### ANSIS Land Use - `ansis:LandUse`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Landform - `ansis:Landform`

Landscape features within which the site is located

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| hasLandformElement | 0..1 | ansis:LandformElement | link to description of landform element |
| hasLandformPattern | 0..1 | ansis:LandformPattern | link to description of landform pattern |
### ANSIS Landform Element - `ansis:LandformElement`

Landform element (~40m).

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| slope | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | divergence of surface from horizontal |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| morphologicalType | 1..1 | sosa:ObservableProperty; skos:Concept | morphological type of landform element |
### ANSIS Landform Pattern - `ansis:LandformPattern`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| relief | 1..1 | sosa:ObservableProperty; skos:Concept | amount of vertical variation of the landform |
| slope | 1..1 | sosa:ObservableProperty; qudt:QuantityValue | divergence of surface from horizontal |
| hasLandformElement | 0..1 | ansis:LandformElement | link to description of landform element |
| hasStreamChannel | 0..1 | ansis:StreamChannel | link to description of stream channel occurrence |
### ANSIS Microrelief - `ansis:Microrelief`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| hasMicrorelief-biotic | 0..1 |  | Undefined. |
| hasMicrorelief-gilgai | 0..1 |  | Undefined. |
| hasMicrorelief-hummocky | 0..1 |  | Undefined. |
| hasMicrorelief-other | 0..1 |  | Undefined. |
### ANSIS Microrelief - Biotic - `ansis:Microrelief_biotic`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| agent | 1..1 | sosa:ObservableProperty; skos:Concept | agent of geomorphological or biotic activity |
### ANSIS Microrelief - Gilgai - `ansis:Microrelief_gilgai`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Microrelief - Hummocky - `ansis:Microrelief_hummocky`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Microrelief - Other - `ansis:Microrelief_other`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Mottles - `ansis:Mottles`

Mottles and other colour patterns.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 0..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
| colour | 0..* |  | link to description of colour |
### ANSIS Outcrop - `ansis:Outcrop`

Rock outcrop.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
| lithology | 1..1 | sosa:ObservableProperty; skos:Concept | lithological type of material |
| relatedLandsurveySite | 0..1 | ansis:LandSurveySite | link to a land survey site related to this context |
| relatedSample | 0..1 | ansis:SoilSample | link to a sample related to this context |
| relatedSite | 0..1 | ansis:SoilSite | link to a soil site related to this context |
### ANSIS Pans - `ansis:Pans`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Pores - `ansis:Pores`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
### ANSIS Profile Purpose - `ansis:Profile-purpose`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Roots - `ansis:Roots`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
### ANSIS Segregations - `ansis:Segregations`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| abundance | 1..1 | sosa:ObservableProperty; skos:Concept | abundance of items |
| material | 1..1 | sosa:ObservableProperty | material or composition of entity or element |
### ANSIS Australian Soil Classification - `ansis:ASC_SoilClassification`

Structure Australian Soil Classification value

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| classificationFamilyA1texture | 0..1 | skos:Concept | family criteria - A1 horizon texture |
| classificationFamilyA1thickness | 0..1 | skos:Concept | family criteria - A1 horizon thickness |
| classificationFamilyBtexture | 0..1 | skos:Concept | family criteria - B horizon texture |
| classificationFamilyDepth | 0..1 | skos:Concept | family criteria - Soil depth |
| classificationFamilyGravel | 0..1 | skos:Concept | family criteria - Gravel of the surface and A1 horizon |
| classificationGreatGroup | 0..1 | skos:Concept | soil classification - Great group |
| classificationOrder | 1..1 | skos:Concept | soil classification - Order |
| classificationSubGroup | 0..1 | skos:Concept | soil classification - Subgroup |
| classificationSubOrder | 0..1 | skos:Concept | soil classification - Sub-order |
### ANSIS Soil Classification - `ansis:SoilClassification`



| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| value | 1..1 | sosa:ObservableProperty; xs:boolean; xs:integer; xs:decimal; xs:string; xs:dateTime | literal value |
| scheme | 1..1 |  | A simple object supporting a link (e.g. a hyperlink) to another entity. |
### ANSIS Soil Horizon Designation - `ansis:HorizonDesignation`

Soil horizon designation. 

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| designationPrefix | 0..1 | xs:integer | soil horizon designation prefix |
| designationSubdivision | 0..1 | xs:integer | soil horizon designation subdivision |
| designationSuffix | 0..1 | skos:Concept | soil horizon designation subdivision |
| designationMaster | 1..1 | skos:Concept | soil horizon designation master |
### ANSIS Soil Colour - `ansis:SoilColour`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| moistureStatus | 1..1 | sosa:ObservableProperty; skos:Concept | moisture state of material while property evaluation is carried out |
| value | 1..1 | sosa:ObservableProperty; xs:boolean; xs:integer; xs:decimal; xs:string; xs:dateTime | literal value |
### ANSIS Soil Plasticity - `ansis:SoilPlasticity`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..1 | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
### ANSIS Soil Sample Type - `ansis:SoilSampleType`

Undefined. [ISSUE: real?]

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Soil Site Design - `ansis:SoilSite-design`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Soil Strength - `ansis:SoilStrength`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| moistureStatus | 1..1 | sosa:ObservableProperty; skos:Concept | moisture state of material while property evaluation is carried out |
| strength | 1..1 | sosa:ObservableProperty; ansis:SoilStrength | strength of material |
### ANSIS Soil Structure - `ansis:SoilStructure`

Soil structure or pedality.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| type | 1..* | ansis:SiteType; ansis:SoilSampleType | type of ansis soil entity |
| grade | 0..1 | sosa:ObservableProperty; skos:Concept | grade or degree of development of structure |
| size | 0..1 | sosa:ObservableProperty; skos:Concept | geometric scale and extent of element |
### ANSIS Site Purpose - `ansis:Site-purpose`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Site Type - `ansis:SiteType`

Type of land survey site e.g. monitoring, opportunistic, farm, pedology.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
### ANSIS Site Visit - `ansis:SiteVisit`

A visit to a designated site, for the purpose of taking samples, making observations, and other activities.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| $schema | 0..1 |  |  |
| @context | 0..1 |  | A link to a JSON-LD Context document that maps property JSON keywords onto OWL/RDF definitions and namespaces (e.g. ansis) onto their base URI. |
| @id | 0..1 |  | An HTTP URI uniquely identifying the object as a Linked Data resource. Dereferencing the URI should, but may not, lead to a JSON or HTML representation of the resource. |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| visitor | 0..1 | prov:Person | site visitor, for the purpose of sampling or observation |
| relatedProject | 1..1 | ansis:Project | link to project that supported this activity |
| relatedLandsurveySite | 0..1 | ansis:LandSurveySite | link to a land survey site related to this context |
| relatedActivity | 1..* | prov:Activity; sosa:Actuation; sosa:Observation; sosa:Sampling; ansis:SiteVisit; ansis:Treatment | link to an activity related to this context |
| relatedSite | 1..1 | ansis:SoilSite | link to a soil site related to this context |
### ANSIS Stream Channel - `ansis:StreamChannel`

Stream channel details.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |
| development | 1..1 | sosa:ObservableProperty; skos:Concept | degree of development of element |
| pattern | 0..1 | sosa:ObservableProperty; skos:Concept | spatial pattern of channels or other linear element |
### ANSIS Survey Design - `ansis:Survey-design`

Undefined.

| Property | Value Count | Type | Description |
| -------- | ----------- | ---- | ----------- |
| @type | 1..1 |  | A compact URI uniquely identifying the type of the object according to the OWL/RDF domain model. |