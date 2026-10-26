package de.schattenarsenal;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.UUID;

import net.fabricmc.fabric.api.entity.event.v1.ServerEntityEvents;
import net.fabricmc.fabric.api.entity.event.v1.ServerLivingEntityEvents;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;
import net.minecraft.ChatFormatting;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.level.ServerBossEvent;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.BossEvent;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.item.ItemEntity;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

/**
 * One independent, stable HUD for each tagged boss. No globally shared bars.
 * The Wither deliberately uses its native vanilla boss bar (no duplicate).
 */
public final class ShadowBosses {
    private ShadowBosses() {}
    private record Hud(LivingEntity boss, ServerBossEvent bar) {}
    private static final Map<UUID, Hud> HUDS = new HashMap<>();

    public static void init() {
        ServerEntityEvents.ENTITY_LOAD.register((entity, world) -> attach(entity));
        ServerEntityEvents.ENTITY_UNLOAD.register((entity, world) -> detach(entity.getUUID()));
        ServerLivingEntityEvents.AFTER_DEATH.register((entity, source) -> {
            String kind = kind(entity);
            if (kind == null || !(entity.level() instanceof ServerLevel level)) return;
            detach(entity.getUUID());
            switch (kind) {
                case "wither" -> {
                    drop(level, entity, enchanted(level, "shadow_chestplate"));
                    drop(level, entity, stack("shadow_wither_core"));
                    drop(level, entity, new ItemStack(Items.NETHER_STAR, 2));
                    drop(level, entity, new ItemStack(Items.CRYING_OBSIDIAN, 8));
                }
                case "warden" -> {
                    drop(level, entity, enchanted(level, "shadow_helmet"));
                    drop(level, entity, stack("shadow_warden_heart"));
                    drop(level, entity, new ItemStack(Items.ECHO_SHARD, 8));
                    drop(level, entity, new ItemStack(Items.SCULK_CATALYST, 2));
                }
                case "knight" -> {
                    drop(level, entity, enchanted(level, "shadow_sword"));
                    drop(level, entity, stack("shadow_knight_sigil"));
                    drop(level, entity, new ItemStack(Items.AMETHYST_SHARD, 12));
                    drop(level, entity, new ItemStack(Items.NETHERITE_SCRAP, 2));
                }
            }
            level.getServer().getPlayerList().broadcastSystemMessage(
                Component.literal("✦ " + label(kind) + " besiegt! Schattenbeute liegt am Kampfplatz.")
                    .withStyle(ChatFormatting.LIGHT_PURPLE), false);
        });
        ServerTickEvents.END_SERVER_TICK.register(server -> {
            Iterator<Map.Entry<UUID, Hud>> it = HUDS.entrySet().iterator();
            while (it.hasNext()) {
                Hud state = it.next().getValue();
                LivingEntity boss = state.boss();
                if (!boss.isAlive() || boss.isRemoved()) {
                    state.bar().removeAllPlayers();
                    it.remove();
                    continue;
                }
                state.bar().setProgress(Math.max(0.0f,
                    Math.min(1.0f, boss.getHealth() / boss.getMaxHealth())));
                for (ServerPlayer player : server.getPlayerList().getPlayers()) {
                    if (player.level() == boss.level()
                            && !player.isSpectator()
                            && player.distanceToSqr(boss) <= 56.0 * 56.0) {
                        state.bar().addPlayer(player);
                    } else {
                        state.bar().removePlayer(player);
                    }
                }
            }
        });
    }

    private static String kind(Entity entity) {
        if (entity.getTags().contains("shadow_wither")) return "wither";
        if (entity.getTags().contains("shadow_warden")) return "warden";
        if (entity.getTags().contains("shadow_knight")) return "knight";
        return null;
    }

    private static String label(String kind) {
        return switch (kind) {
            case "warden" -> "Schatten-Warden";
            case "knight" -> "Schattenritter";
            default -> "Violetter Schatten-Wither";
        };
    }

    private static void attach(Entity entity) {
        if (!(entity instanceof LivingEntity living)) return;
        String kind = kind(entity);
        if (kind == null || kind.equals("wither") || HUDS.containsKey(entity.getUUID())) return;
        ServerBossEvent bar = new ServerBossEvent(
            Component.literal("✦ " + label(kind) + " ✦").withStyle(ChatFormatting.LIGHT_PURPLE),
            BossEvent.BossBarColor.PURPLE, BossEvent.BossBarOverlay.PROGRESS);
        bar.setProgress(1.0f);
        HUDS.put(entity.getUUID(), new Hud(living, bar));
    }

    private static void detach(UUID uuid) {
        Hud hud = HUDS.remove(uuid);
        if (hud != null) hud.bar().removeAllPlayers();
    }

    private static ItemStack stack(String id) {
        return new ItemStack(SchattenArsenal.ITEMS.get(id));
    }

    private static ItemStack enchanted(ServerLevel level, String id) {
        ItemStack stack = stack(id);
        var lookup = level.registryAccess().lookupOrThrow(Registries.ENCHANTMENT);
        for (String name : SchattenArsenal.ENCHANTS.getOrDefault(id, "").split(",")) {
            if (name.isEmpty()) continue;
            ResourceKey<net.minecraft.world.item.enchantment.Enchantment> key = ResourceKey.create(
                Registries.ENCHANTMENT, Identifier.fromNamespaceAndPath("minecraft", name));
            lookup.get(key).ifPresent(holder -> stack.enchant(holder, 50));
        }
        return stack;
    }

    private static void drop(ServerLevel level, Entity mob, ItemStack stack) {
        ItemEntity item = new ItemEntity(level,
            mob.getX(), mob.getY() + 0.4, mob.getZ(), stack);
        level.addFreshEntity(item);
    }
}
