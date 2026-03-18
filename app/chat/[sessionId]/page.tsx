import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { redirect } from "next/navigation";
import { ChatWindow } from "@/components/chat/ChatWindow";

interface Props {
  params: { sessionId: string };
}

export default async function ChatSessionPage({ params }: Props) {
  const session = await getServerSession(authOptions);
  if (!session) redirect("/login");
  if (!session.user.name) redirect("/onboarding");

  return <ChatWindow sessionId={params.sessionId} />;
}
