// Data Services Bicep module

@description('Location for all resources')
param location string

@description('Environment name')
param environment string

@description('Unique suffix for resource names')
param uniqueSuffix string

// Azure Cognitive Search
resource search 'Microsoft.Search/searchServices@2023-11-01' = {
  name: 'search-${environment}-${uniqueSuffix}'
  location: location
  sku: {
    name: 'basic'
  }
}

// Azure Cosmos DB
resource cosmos 'Microsoft.DocumentDB/databaseAccounts@2023-04-15' = {
  name: 'cosmos-${environment}-${uniqueSuffix}'
  location: location
  properties: {
    databaseAccountOfferType: 'Standard'
    capabilities: [
      {
        name: 'EnableGremlin'
      }
    ]
    locations: [
      {
        locationName: location
        failoverPriority: 0
      }
    ]
  }
}

// Azure Storage
resource storage 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'storage${environment}${uniqueSuffix}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// Outputs
output searchEndpoint string = 'https://${search.name}.search.windows.net'
output cosmosEndpoint string = cosmos.properties.documentEndpoint
output storageEndpoint string = storage.properties.primaryEndpoints.blob
