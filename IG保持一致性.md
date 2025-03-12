twcore Implemetation Guide 實作package, definition時 如何保持一致性
在實現 TwCore Implementation Guide（IG）時，保持一致性是確保系統與 TwCore 規範兼容的重要任務。以下是實現過程中保持一致性的方法和實踐：
1. 使用標准工具保持一致性
    • FHIR Validator：使用 FHIR Validator 工具驗證您的 FHIR 資源是否符合 TwCore 的 StructureDefinition、ValueSets 和 CodeSystems。FHIR Validator 能夠自動檢查資源的格式、結構和編碼系統是否符合規範。
        ◦ 下載 FHIR Validator：https://simplifier.net/guide/fhirvalidator
        ◦ 使用方法：
          java -jar validator_cli.jar <resource-file>.json -ig <twcore-IG-package>
    • IG Publisher：FHIR Implementation Guide Publisher 是官方提供的工具，用於驗證和發布 FHIR Implementation Guide。通過該工具，您可以在本地驗證并搆建 IG，確保與 TwCore 的定義保持一致。
        ◦ IG Publisher：https://confluence.hl7.org/display/FHIR/IG+Publisher+Documentation
2. 遵循 CapabilityStatement
TwCore Implementation Guide 中的 CapabilityStatement 描述了服務器支持的 FHIR 資源、操作和交互。通過 CapabilityStatement，您可以確保：
    • 實現的資源類型與 TwCore 的要求一致。
    • 支持的操作（如 create、read、update、delete）符合 TwCore 的規範。
    • 支持的交互模式（如 RESTful API 的調用方式）與 TwCore 一致。
確保一致性的步驟：
    • 獲取 TwCore FHIR 服務器的 /metadata 端點輸出。
    • 確認所實現的資源、操作和交互是否與 CapabilityStatement 中列出的要求相符。
3. 使用 TwCore 的 StructureDefinition
TwCore IG 提供的 StructureDefinition 文件定義了 FHIR 資源的具體約束、擴展和裁剪。這是保持資源一致性的核心內容。使用以下步驟保持一致性：
    • 下載 TwCore 的 Package 文件，其中包含所有 TwCore 的 StructureDefinition 資源。
    • 應用 StructureDefinition 的約束：在實現 FHIR 資源時，遵循 TwCore 定義的約束，確保所生成的數據結構與標准 FHIR 資源格式一致。
        ◦ 例如，某個 Patient 資源的姓名字段可能在 TwCore 中有特定的格式或要求（如必填字段、特定編碼系統等），實現時應確保遵守這些規則。
    • 使用擴展：如果 TwCore IG 包含對標准 FHIR 資源的擴展，確保在實現中正確使用這些擴展，并保持擴展格式與 IG 中的定義一致。
4. 處理 ValueSets 和 CodeSystems
TwCore Implementation Guide 中的 ValueSets 和 CodeSystems 資源定義了特定字段的可接受值和編碼系統。為了確保與 TwCore 的一致性，您需要：
    • 引入 TwCore 的 ValueSets 和 CodeSystems：將 TwCore IG 提供的 ValueSets 和 CodeSystems 集成到系統中，確保所有字段的值和編碼與 TwCore 定義的值集保持一致。
    • 驗證編碼值：在提交或接收數據時，使用 TwCore 提供的 ValueSets 驗證數據的正確性，確保編碼系統與 TwCore 的定義相符。
5. 自動化測試
自動化測試是確保一致性的關鍵步驟。可以通過以下方式實現自動化測試：
    • 單元測試：編寫測試用例，確保所生成的 FHIR 資源符合 TwCore 的 StructureDefinition 和 ValueSets。
    • 集成測試：模擬真實場景下的 FHIR 數據交換，測試系統在 TwCore 的各類操作中（如創建、讀取、更新、刪除資源）能否正確處理數據。
    • FHIR Validator 集成：將 FHIR Validator 集成到 CI/CD 管道中，在每次提交代碼時自動運行驗證，確保所生成的資源符合 TwCore 的規範。
6. 使用示例資源和測試用例
TwCore Implementation Guide 通常會提供一些 示例資源（Example Resources）和 測試用例，以幫助開發人員理解資源的正確實現方式。通過使用這些示例資源，您可以：
    • 參考示例資源：這些資源展示了 TwCore 如何自定義 FHIR 資源，您可以將其作為參考來實現自己的系統。
    • 進行數據驗證：生成的 FHIR 資源可以與 TwCore 提供的示例資源進行比較，確保字段名稱、值、編碼系統、擴展等保持一致。
    • 運行測試用例：如果 TwCore 提供了相關測試用例或測試套件（如基於 FHIR TestScript 資源的測試），您可以使用這些測試來驗證實現的資源。
7. 定期更新和同步 TwCore IG
    • FHIR 標准和 Implementation Guide 可能會定期更新，因此保持一致性的另一個重要部分是定期檢查和同步 TwCore Implementation Guide。
    • 保持版本同步：確保使用 TwCore 最新版本的 IG package。關注 TwCore 社區或官方網站，獲取最新的 IG 更新和變更。
    • 重新驗證和調整：在 TwCore IG 更新時，使用 FHIR Validator 等工具重新驗證現有的實現，必要時進行調整以符合最新版本的要求。
8. Documentation 和開發團隊的協作
    • 確保開發團隊對 TwCore 的 FHIR 規範和定義有清晰的理解，并保持文檔的更新和共享。
    • 內部標准：根據 TwCore IG 規範，制定一套內部標准和開發指南，明確每個 FHIR 資源的實現方式、擴展使用規則等。
    • 開發文檔更新：每次 IG 版本更新后，開發團隊應更新內部開發文檔，并確保所有新開發或維護的系統模塊遵守新的規範。
總結
為了在實現 TwCore Implementation Guide 的過程中保持一致性，您需要：
    • 使用 FHIR Validator 和 IG Publisher 工具進行驗證。
    • 遵循 TwCore 的 CapabilityStatement，確保所實現的資源、操作和交互符合規範。
    • 使用 TwCore 提供的 StructureDefinition、ValueSets 和 CodeSystems 實現和驗證資源。
    • 通過自動化測試、定期更新和協作開發來確保系統始終與 TwCore 規範保持一致。
