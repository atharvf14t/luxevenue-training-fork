import OpenAI from 'openai';

export function createAzureClient() {
  return new OpenAI({
    apiKey: process.env.AZURE_OPENAI_API_KEY!,
    baseURL: `${process.env.AZURE_OPENAI_ENDPOINT}openai/deployments/${process.env.AZURE_OPENAI_DEPLOYMENT}`,
    defaultQuery: { 'api-version': process.env.AZURE_OPENAI_API_VERSION ?? '2024-08-01-preview' },
    defaultHeaders: { 'api-key': process.env.AZURE_OPENAI_API_KEY! },
  });
}

export function createOpenAIImageClient() {
  return new OpenAI({
    apiKey: process.env.OPENAI_API_KEY!,
  });
}
