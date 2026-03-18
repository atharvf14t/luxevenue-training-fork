import { prisma } from './prisma';

export type QuotaResult =
  | { allowed: true }
  | { allowed: false; reason: 'not_enabled' | 'quota_exceeded' };

export async function checkImageQuota(userId: string): Promise<QuotaResult> {
  const user = await prisma.user.findUnique({
    where: { id: userId },
    select: { maxImages: true },
  });

  if (!user || user.maxImages === 0) {
    return { allowed: false, reason: 'not_enabled' };
  }

  const used = await prisma.imageGeneration.count({ where: { userId } });

  if (used >= user.maxImages) {
    return { allowed: false, reason: 'quota_exceeded' };
  }

  return { allowed: true };
}
