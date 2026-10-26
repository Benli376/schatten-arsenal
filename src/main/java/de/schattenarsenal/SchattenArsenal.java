package de.schattenarsenal;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.creativetab.v1.FabricCreativeModeTab;
import net.minecraft.core.Registry;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.util.Unit;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;

import java.util.LinkedHashMap;
import java.util.Map;

public class SchattenArsenal implements ModInitializer {
    private static final Map<String, Item> ITEMS = new LinkedHashMap<>();
    private static Item register(String name) {
        Identifier id = Identifier.fromNamespaceAndPath("schattenarsenal", name);
        ResourceKey<Item> key = ResourceKey.create(Registries.ITEM, id);
        Item item = Registry.register(BuiltInRegistries.ITEM, key,
            new Item(new Item.Properties().setId(key).fireResistant().component(DataComponents.UNBREAKABLE, Unit.INSTANCE)));
        ITEMS.put(name, item);
        return item;
    }

    @Override public void onInitialize() {
        for (String name : new String[] {"shadow_helmet","shadow_chestplate","shadow_leggings","shadow_boots",
                "shadow_sword","shadow_pickaxe","shadow_axe","shadow_shovel","shadow_hoe",
                "shadow_wither_spawn_egg","shadow_warden_spawn_egg","shadow_knight_spawn_egg"}) {
            register(name);
        }
        ResourceKey<CreativeModeTab> key = ResourceKey.create(Registries.CREATIVE_MODE_TAB,
            Identifier.fromNamespaceAndPath("schattenarsenal","shadow_arsenal"));
        CreativeModeTab tab = FabricCreativeModeTab.builder()
            .title(Component.literal("Schatten-Arsenal"))
            .icon(() -> new ItemStack(ITEMS.get("shadow_sword")))
            .displayItems((params, output) -> ITEMS.values().forEach(item -> output.accept(new ItemStack(item))))
            .build();
        Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB, key, tab);
    }
}
