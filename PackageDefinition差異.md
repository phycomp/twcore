twcore Implemetation Guide package, definition 的差異
在 TwCore Implementation Guide（IG）中，package 和 definition 是實現 FHIR 資源時的兩個關鍵概念，它們在作用和用途上有所不同。以下是二者的差異：
1. Package 和 Definition 的定義
Package
    • Package 是 Implementation Guide 中包含的一個壓縮包或一組資源文件的集合，通常用於傳遞和分享整個 Implementation Guide 的內容。它包含了所有實現某個 FHIR 標准或自定義擴展所需的 FHIR 資源、Profile、ValueSet、CodeSystem、OperationDefinition 等文件。
    • 內容：
        ◦ StructureDefinition（結構定義）：對標准 FHIR 資源的擴展或約束。
        ◦ ValueSet 和 CodeSystem：特定數據字段的值集和編碼系統。
        ◦ OperationDefinition：自定義操作定義。
        ◦ CapabilityStatement：列出該 FHIR 服務支持的資源和操作。
    • 功能：提供了所有與 TwCore Implementation Guide 相關的規範資源和依賴，便於開發者實現和部署相關的 FHIR 服務。
    • 用途：Package 是一個打包好的文件，可以直接用於系統集成、配置和發布。開發者可以通過下載并引入該 package 來確保所開發的系統符合 TwCore 的標准。
Definition
    • Definition 是 Implementation Guide 中對如何實現、使用或擴展 FHIR 資源的具體指導文檔。它提供了關於具體資源和操作的詳細規範。
    • 內容：
        ◦ 對每個 FHIR 資源及其字段的詳細定義和解釋。
        ◦ 資源的使用方式、約束條件和擴展點（如哪些字段是必填，哪些字段允許自定義擴展）。
        ◦ 指導如何在實際業務場景中應用這些資源，包括業務規則、數據流及其關聯的交互操作。
    • 功能：提供了實現 FHIR 資源的明確指導，確保開發人員理解并正確應用 Implementation Guide 中定義的內容。
    • 用途：開發人員通過閱讀和參考 Definition，了解如何在其系統中實現 TwCore 定義的 FHIR 資源。Definition 還包括擴展的使用方法和如何與其他資源交互。
2. 用途與實現中的差異
Package 的用途
    • 包管理與分發：Package 是將 TwCore Implementation Guide 的所有相關資源打包成一個整體，便於在不同系統中統一分發和部署。它包括了所有資源的定義，可以直接導入到 FHIR 服務器或集成環境中。
    • 快速集成：開發者可以直接下載 Package 并在其系統中導入這些資源，無需手動配置各個文件。Package 文件在實現過程中有助於減少配置和初始化的復雜性。
Definition 的用途
    • 詳細規範與實現指導：Definition 側重於說明如何使用 Package 中的資源。開發者通過查看 Definition，了解如何使用 StructureDefinition 進行字段約束、使用 ValueSet 進行值驗證、如何擴展標准 FHIR 資源等。
    • 約束與擴展說明：Definition 說明了哪些字段是必須的、哪些可以擴展，以及如何處理特定的業務場景。例如，某個資源可能在 TwCore 實現中需要額外的字段，這些信息會在 Definition 中詳細描述。
3. 主要差異總結
項目	Package	Definition
本質	資源的集合，通常是 .zip 文件或包	對資源及其使用方法的詳細說明
功能	包含所有實現所需的文件	解釋如何實現和使用這些資源
包含內容	StructureDefinition、ValueSet、CodeSystem 等資源	對資源的字段定義、業務規則、約束和擴展的描述
應用場景	開發時用於導入到系統或 FHIR 服務器	作為開發時的參考，用於理解如何具體實現資源
實施方法	包文件可以直接使用，減少手動配置的工作	通過閱讀并理解 Definition，正確實現業務邏輯
開發者使用方式	下載并導入包，實現快速集成	通過定義文件理解具體的資源結構和實現方式
4. 實例舉例
Package 的作用：
假設您要實現 TwCore 中的 Patient 資源。您可以從 TwCore 的 Implementation Guide 中下載整個 Package，解壓后獲得 StructureDefinition-Patient.json 文件，這個文件定義了 TwCore 對標准 FHIR Patient 資源的自定義約束，比如新增的擴展字段或特定字段的格式要求。您可以將這個文件導入系統中，并使用它自動驗證患者數據的結構。
Definition 的作用：
Definition 文件則會詳細解釋如何實現 Patient 資源，比如：
    • 必須包含哪些字段（例如name 和 gender 是必填字段）。
    • 某些字段是否可以擴展（例如，您可以添加額外的聯系方式擴展）。
    • 業務規則（例如，birthDate 必須早於當前日期，且格式必須符合 YYYY-MM-DD）。
5. 保持一致性的方式
    • 通過 Package 實現自動化：使用 TwCore 提供的 Package 資源，確保您的系統始終使用相同的 StructureDefinition、ValueSet 和 CodeSystem，從而避免人為錯誤。
    • 通過 Definition 理解約束：在實際開發過程中，參考 Definition 文件來理解 Package 中資源的具體使用場景、擴展點和業務邏輯，以確保您實現的邏輯符合 TwCore 的定義。
總結
    • Package 是 TwCore Implementation Guide 的資源集合，主要用於快速集成、導入和分發。它包含所有實現資源的文件。
    • Definition 是對 Package 中資源的詳細說明和使用指南，幫助開發人員正確實現資源并遵守業務規則。
兩者在實現時相輔相成，Package 提供具體的資源文件，而 Definition 則提供如何使用這些資源的詳細指導。
