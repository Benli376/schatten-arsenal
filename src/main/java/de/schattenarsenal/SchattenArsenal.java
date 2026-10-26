package de.schattenarsenal;

import net.fabricmc.api.ModInitializer;
import net.fabricmc.fabric.api.creativetab.v1.FabricCreativeModeTab;
import net.minecraft.core.Registry;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.nbt.ListTag;
import net.minecraft.nbt.StringTag;
import net.minecraft.world.item.component.TypedEntityData;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.Identifier;
import net.minecraft.resources.ResourceKey;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.tags.TagKey;
import net.minecraft.util.Unit;
import net.minecraft.world.item.equipment.ArmorMaterial;
import net.minecraft.world.item.AxeItem;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.HoeItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.ShovelItem;
import net.minecraft.world.item.SpawnEggItem;
import net.minecraft.world.item.ToolMaterial;
import net.minecraft.world.item.equipment.ArmorType;
import net.minecraft.world.item.equipment.EquipmentAsset;
import net.minecraft.world.item.equipment.EquipmentAssets;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.entity.EntityType;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.function.Function;

public class SchattenArsenal implements ModInitializer {
    public static final String MOD_ID="schattenarsenal";
    static Identifier id(String path) {return Identifier.fromNamespaceAndPath(MOD_ID,path);}
    static final Map<String,Item> ITEMS=new LinkedHashMap<>();
    static final TagKey<Item> REPAIR=TagKey.create(Registries.ITEM,id("shadow_repair"));
    static final TagKey<Block> INCORRECT=TagKey.create(Registries.BLOCK,id("incorrect_for_shadow_tool"));
    static final ResourceKey<EquipmentAsset> EQUIPMENT=ResourceKey.create(EquipmentAssets.ROOT_ID,id("shadow"));
    static final ArmorMaterial ARMOR=new ArmorMaterial(37,
        Map.of(ArmorType.HELMET,3,ArmorType.CHESTPLATE,8,ArmorType.LEGGINGS,6,ArmorType.BOOTS,3),
        20, SoundEvents.ARMOR_EQUIP_NETHERITE,3.0F,0.1F,REPAIR,EQUIPMENT);
    static final ToolMaterial TOOL=new ToolMaterial(INCORRECT,3000,12.0F,6.0F,20,REPAIR);

    // Level 50: positive enchantments only; no Fortune, Frost Walker or curses.
    private static final Map<String,String> ENCHANTS=Map.ofEntries(
      Map.entry("shadow_helmet","protection,fire_protection,blast_protection,projectile_protection,respiration,aqua_affinity,thorns,unbreaking,mending"),
      Map.entry("shadow_chestplate","protection,fire_protection,blast_protection,projectile_protection,thorns,unbreaking,mending"),
      Map.entry("shadow_leggings","protection,fire_protection,blast_protection,projectile_protection,swift_sneak,thorns,unbreaking,mending"),
      Map.entry("shadow_boots","protection,fire_protection,blast_protection,projectile_protection,feather_falling,depth_strider,soul_speed,thorns,unbreaking,mending"),
      Map.entry("shadow_sword","sharpness,smite,bane_of_arthropods,knockback,fire_aspect,looting,sweeping_edge,unbreaking,mending"),
      Map.entry("shadow_pickaxe","efficiency,silk_touch,unbreaking,mending"),
      Map.entry("shadow_axe","efficiency,silk_touch,sharpness,smite,bane_of_arthropods,unbreaking,mending"),
      Map.entry("shadow_shovel","efficiency,silk_touch,unbreaking,mending"),
      Map.entry("shadow_hoe","efficiency,silk_touch,unbreaking,mending")
    );

    private static TypedEntityData<EntityType<?>> shadowBossData(String entityId,String tag,String name) {
        EntityType<?> type=BuiltInRegistries.ENTITY_TYPE.getValue(Identifier.fromNamespaceAndPath("minecraft",entityId));
        CompoundTag nbt=new CompoundTag();
        ListTag tags=new ListTag();
        tags.add(StringTag.valueOf(tag));
        nbt.put("Tags",tags);
        nbt.putBoolean("PersistenceRequired",true);
        nbt.putString("CustomName","{\"text\":\""+name+"\",\"color\":\"dark_purple\",\"bold\":true}");
        return TypedEntityData.of(type,nbt);
    }

    private static ItemStack enchanted(String name,Item item, CreativeModeTab.ItemDisplayParameters params) {
        ItemStack stack=new ItemStack(item);
        String enchantNames=ENCHANTS.get(name);
        if (enchantNames != null) {
            var lookup=params.holders().lookupOrThrow(Registries.ENCHANTMENT);
            for (String enchantName:enchantNames.split(",")) {
                var key=ResourceKey.create(Registries.ENCHANTMENT,Identifier.fromNamespaceAndPath("minecraft",enchantName));
                lookup.get(key).ifPresent(holder -> stack.enchant(holder,50));
            }
        }
        return stack;
    }

    static Item.Properties unbreakable(){return new Item.Properties().fireResistant().component(DataComponents.UNBREAKABLE, Unit.INSTANCE);}
    static void register(String name,Function<Item.Properties,Item> maker,Item.Properties props){
        ResourceKey<Item> key=ResourceKey.create(Registries.ITEM,id(name));
        Item item=Registry.register(BuiltInRegistries.ITEM,key,maker.apply(props.setId(key)));
        ITEMS.put(name,item);
    }
    public void onInitialize(){
        register("shadow_helmet",Item::new,unbreakable().humanoidArmor(ARMOR,ArmorType.HELMET).durability(ArmorType.HELMET.getDurability(37)));
        register("shadow_chestplate",Item::new,unbreakable().humanoidArmor(ARMOR,ArmorType.CHESTPLATE).durability(ArmorType.CHESTPLATE.getDurability(37)));
        register("shadow_leggings",Item::new,unbreakable().humanoidArmor(ARMOR,ArmorType.LEGGINGS).durability(ArmorType.LEGGINGS.getDurability(37)));
        register("shadow_boots",Item::new,unbreakable().humanoidArmor(ARMOR,ArmorType.BOOTS).durability(ArmorType.BOOTS.getDurability(37)));
        register("shadow_sword",Item::new,unbreakable().sword(TOOL,6f,-2.4f));
        register("shadow_pickaxe",Item::new,unbreakable().pickaxe(TOOL,1f,-2.8f));
        register("shadow_axe",p->new AxeItem(TOOL,6f,-3.0f,p),unbreakable());
        register("shadow_shovel",p->new ShovelItem(TOOL,1.5f,-3.0f,p),unbreakable());
        register("shadow_hoe",p->new HoeItem(TOOL,-4f,0f,p),unbreakable());
        register("shadow_wither_spawn_egg",SpawnEggItem::new,new Item.Properties().spawnEgg(BuiltInRegistries.ENTITY_TYPE.getValue(Identifier.fromNamespaceAndPath("minecraft","wither"))).component(DataComponents.ENTITY_DATA,shadowBossData("wither","shadow_wither","Violetter Schatten-Wither")));
        register("shadow_warden_spawn_egg",SpawnEggItem::new,new Item.Properties().spawnEgg(BuiltInRegistries.ENTITY_TYPE.getValue(Identifier.fromNamespaceAndPath("minecraft","warden"))).component(DataComponents.ENTITY_DATA,shadowBossData("warden","shadow_warden","Schatten-Warden")));
        register("shadow_knight_spawn_egg",SpawnEggItem::new,new Item.Properties().spawnEgg(BuiltInRegistries.ENTITY_TYPE.getValue(Identifier.fromNamespaceAndPath("minecraft","wither_skeleton"))).component(DataComponents.ENTITY_DATA,shadowBossData("wither_skeleton","shadow_knight","Schattenritter")));

        ResourceKey<CreativeModeTab> key=ResourceKey.create(Registries.CREATIVE_MODE_TAB,id("shadow_arsenal"));
        CreativeModeTab tab=FabricCreativeModeTab.builder().title(Component.literal("Schatten-Arsenal"))
            .icon(()->new ItemStack(ITEMS.get("shadow_sword")))
            .displayItems((params,out)->ITEMS.forEach((name,item)->out.accept(enchanted(name,item,params)))).build();
        Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB,key,tab);
    }
}
