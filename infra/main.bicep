// Main Bicep template for Universal RAG Azure

@description('Location for all resources')
param location string = resourceGroup().location

@description('Environment name')
param environment string = 'dev'

@description('Unique suffix for resource names')
param uniqueSuffix string = uniqueString(resourceGroup().id)

// Deploy AI services
module aiServices 'modules/ai-services.bicep' = {
  name: 'ai-services-deployment'
  params: {
    location: location
    environment: environment
    uniqueSuffix: uniqueSuffix
  }
}

// Deploy data services
module dataServices 'modules/data-services.bicep' = {
  name: 'data-services-deployment'
  params: {
    location: location
    environment: environment
    uniqueSuffix: uniqueSuffix
  }
}

// Outputs
output openaiEndpoint string = aiServices.outputs.openaiEndpoint
output searchEndpoint string = dataServices.outputs.searchEndpoint
output cosmosEndpoint string = dataServices.outputs.cosmosEndpoint
output storageEndpoint string = dataServices.outputs.storageEndpoint
