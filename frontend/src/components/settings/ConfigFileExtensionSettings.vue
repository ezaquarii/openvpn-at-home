<template>
    <form class="ui form" @submit.prevent="handleSubmit">
        <div class="content">
            <!-- TODO Remove hardcoding of available extensions -->
            <div class="field">
                <div class="ui radio checkbox">
                    <input id="ovpn" v-model="settings.config_file_extension" type="radio" value="ovpn">
                    <label for="ovpn">OVPN</label>
                </div>
            </div>
            <div class="field">
                <div class="ui radio checkbox">
                    <input id="conf" v-model="settings.config_file_extension" type="radio" value="conf">
                    <label for="conf">CONF</label>
                </div>
            </div>
            <div class="field">
                <button type="submit" class="ui button settings-button" role="button" @submit="{}">Save</button>
            </div>
        </div>
    </form>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator';
import NavigationBar from '@/components/NavigationBar.vue';
import _ from 'lodash';

@Component({
    name: 'ConfigFileExtensionSettings',
    components: {
        NavigationBar
    }
})
export default class ConfigFileExtensionSettings extends Vue {

        settings = {
            config_file_extension: 'conf'
        };

        handleSubmit () {
            this.$store.dispatch('setSettings', this.settings);
        }

        mounted () {
            this.settings.config_file_extension = _.cloneDeep(this.$store.state.settings.config_file_extension);
        }

}

</script>

<style scoped lang="scss">

</style>
